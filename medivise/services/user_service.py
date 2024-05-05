from bson import ObjectId

from medivise.models.user import User
from medivise.utils.mongo_client import db


class UserService:
    def __init__(self):
        self.users = db["users"]

    def register_user(self, user: User):
        user_json = user.model_dump()
        response = self.users.insert_one(user_json)
        return response.inserted_id

    def get_user(self, user_id: str) -> User:
        user = self.users.find_one({'_id': ObjectId(user_id)})
        if user is None:
            return None
        return User(**user)

    def update_user(self, user: User):
        user_json = user.model_dump()
        response = self.users.update_one({'_id': user.id}, {'$set': user_json})
        return response.modified_count

    def delete_user(self, user_id: str):
        response = self.users.delete_one({'_id': user_id})
        return response.deleted_count

    def get_all_users(self) -> list[User]:
        users = self.users.find()
        return [User.model_load(user) for user in users]
