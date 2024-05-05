from pydantic import Field

from medivise.enums.medication_type import MedicineType
from medivise.enums.strength_unit import StrengthUnit
from medivise.enums.weekdays import Weekday
from medivise.models.base_model import BaseModelEncoder
from medivise.models.pyobject import PyObjectId


class Medication(BaseModelEncoder):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    brand_name: str
    generic_name: str
    type: MedicineType
    strength: float
    unit: StrengthUnit
    frequency: list[Weekday]
    notes: str
    purpose: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_id": "6606bd42300fb88a50c3fd48",
                    "brand_name": "Crocin",
                    "generic_name": "Paracetamol",
                    "type": MedicineType.tablet,
                    "strength": 500,
                    "unit": StrengthUnit.mg,
                    "frequency": [Weekday.MONDAY, Weekday.WEDNESDAY],
                    "notes": "Take after breakfast",
                    "purpose": "For fever"
                }
            ]
        }
    }
