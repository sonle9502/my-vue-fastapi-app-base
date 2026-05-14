from fastapi import HTTPException


def require_roles(user, allowed_roles: list[str]):

    roles = user.get("realm_access", {}).get("roles", [])

    has_permission = any(
        role in roles for role in allowed_roles
    )

    if not has_permission:

        raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )