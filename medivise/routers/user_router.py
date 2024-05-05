from fastapi import APIRouter

from medivise.models.user import User
from medivise.services.user_service import UserService

router = APIRouter()


@router.post("/health-details", tags=["health-details"])
def create_user(user: User):
    user_id = UserService().register_user(user)
    return UserService().get_user(user_id)
