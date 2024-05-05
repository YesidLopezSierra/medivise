
from pydantic import Field

from medivise.enums.blood_type import BloodType
from medivise.enums.gender import Gender
from medivise.models.base_model import BaseModelEncoder
from medivise.models.pyobject import PyObjectId


class User(BaseModelEncoder):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    height: int
    weight: int
    age: int
    gender: Gender
    blood_type: BloodType
    allergies: list[str] = []
    medical_conditions: list[str] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "height": 175,
                    "weight": 70,
                    "age": 25,
                    "name": "Sara",
                    "gender": Gender.MALE,
                    "blood_type": BloodType.A_POSITIVE,
                    "allergies": ["Peanuts", "Lactose"],
                    "medical_conditions": ["Asthma", "Diabetes"]
                }
            ]
        }
    }
