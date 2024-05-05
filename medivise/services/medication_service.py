import json

from bson import ObjectId

from medivise.enums.medication_type import MedicineType
from medivise.enums.strength_unit import StrengthUnit
from medivise.models.medication import Medication
from medivise.services.user_service import UserService
from medivise.utils import chain
from medivise.utils.llm import llm
from medivise.utils.mongo_client import db


class MedicationService:
    def __init__(self):
        self.db = db
        self.medications = self.db['medications']

    def get_medications(self, user_id: str):
        user = UserService().get_user(user_id)
        if user is None:
            raise ValueError("The user does not exist")

        medications = self.medications.find({"user_id": ObjectId(user_id)})
        return [Medication(**medication) for medication in medications]

    def get_medication(self, user_id: str, medication_id: str):
        user = UserService().get_user(user_id)
        if user is None:
            raise ValueError("The user does not exist")

        medication = self.medications.find_one(
            {"_id": ObjectId(medication_id)})
        if medication is None:
            raise ValueError("The medication does not exist")

        return Medication(**medication)

    def register_medications(self, medications: list[Medication]):
        for medication in medications:
            user = UserService().get_user(medication.user_id)
            if user is None:
                raise ValueError("The user does not exist")

        medications_json = [medication.model_dump()
                            for medication in medications]
        inserted_ids = self.medications.insert_many(
            medications_json).inserted_ids
        return [str(id) for id in inserted_ids]

    def analyze_text(self, text: str):
        prompt = f"""
        Consider the following information of a medication
        Medication info: {text}

        extract the following properties:
        - "brand_name": the brand name of the medication
        - "generic_name": the generic name of the medication
        - "type": use as value only the following options: {[type.value for type in MedicineType]}
        - "strength": strength of the medication.
        - "unit": the unit of the strength. use as value only the following options: {[unit.value for unit in StrengthUnit]}
        - "purpose": for what kind of illness the medication is used

        Do not use markdown.
        JSON:
        """
        response = llm.invoke(prompt)
        return json.loads(response.content)

    def check_interactions(self, medicine_a: str, medicine_b: str):
        interactions = chain.interactions_chain(
            medicine_a=medicine_a, medicine_b=medicine_b)
        return {**interactions, "medicine_a": medicine_a, "medicine_b": medicine_b}
