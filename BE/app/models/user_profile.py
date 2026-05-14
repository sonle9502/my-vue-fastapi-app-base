from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.base import Base


class UserProfile(Base):
    __tablename__ = "user_profile"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    keycloak_id = Column(String, unique=True, nullable=False)

    username = Column(String)
    email = Column(String)

    full_name = Column(String)
    phone = Column(String)

    avatar_url = Column(String)