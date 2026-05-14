from pydantic import BaseModel


class UpdateProfileRequest(BaseModel):
    full_name: str | None = None
    phone: str | None = None
    avatar_url: str | None = None