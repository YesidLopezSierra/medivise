from typing import Optional

from medivise.enums.medication_type import MedicineType
from medivise.enums.strength_unit import StrengthUnit
from medivise.models.response_body.base_model import BaseModelPayload


class MedicineDetailsExtractedPayload(BaseModelPayload):
    brand_name: Optional[str] = None
    generic_name: Optional[str] = None
    type: Optional[MedicineType] = None
    strength: Optional[float] = None
    unit: Optional[StrengthUnit] = None
    purpose: Optional[str] = None
