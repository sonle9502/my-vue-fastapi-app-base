from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.keycloak_auth import get_current_user
from app.auth.permissions import require_roles
from app.database.deps import get_db
from app.models.user_profile import UserProfile
from app.schemas.user_schema import UpdateProfileRequest

router = APIRouter()


@router.get("/api/me")
def get_me(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    username = user.get("preferred_username")
    print(UserProfile.username)

    profile = db.query(UserProfile).filter(
        UserProfile.username == username
    ).first()

    # 🔥 Auto create profile
    if not profile:
        profile = UserProfile(
            keycloak_id=user.get("sub"),
            username=username,
            email=user.get("email"),
            full_name=user.get("name"),
        )

        db.add(profile)
        db.commit()
        db.refresh(profile)

    return {
    "id": str(profile.id),
    "username": profile.username,
    "email": profile.email,
    "full_name": profile.full_name,
    "phone": profile.phone,
    "avatar_url": profile.avatar_url,
    "roles": user.get("realm_access", {}).get("roles", []),
    }


@router.put("/api/me")
def update_me(
    payload: UpdateProfileRequest,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    require_roles(user, ["admin"])
    username = user.get("preferred_username")

    profile = db.query(UserProfile).filter(
        UserProfile.username == username
    ).first()

    if not profile:
        return {"message": "Profile not found"}

    profile.full_name = payload.full_name
    profile.phone = payload.phone
    profile.avatar_url = payload.avatar_url

    db.commit()
    db.refresh(profile)

    return {
        "message": "Update successful123",
        "profile": profile
    }