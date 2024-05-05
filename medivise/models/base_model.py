
from bson import ObjectId
from pydantic import BaseModel


class BaseModelEncoder(BaseModel):
    class Config:
        json_encoders = {ObjectId: str}
        use_enum_values = True
