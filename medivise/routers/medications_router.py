from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException

from medivise.models.medication import Medication
from medivise.models.response_body.medicine_details import \
    MedicineDetailsExtractedPayload
from medivise.services.medication_service import MedicationService

router = APIRouter()


@router.get("/user/{user_id}/medications", tags=["medications"])
def get_medications(user_id: str):
    try:
        medications = MedicationService().get_medications(user_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except InvalidId as ie:
        raise HTTPException(status_code=404, detail=str(ie))
    return medications


@router.get("/user/{user_id}/medication/{medication_id}", tags=["medications"])
def get_medication(user_id: str, medication_id: str):
    try:
        medications = MedicationService().get_medication(user_id, medication_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except InvalidId as ie:
        raise HTTPException(status_code=404, detail=str(ie))
    return medications


@router.post("/medications", tags=["medications"])
def add_medications(medications: list[Medication]):
    try:
        medication_ids = MedicationService().register_medications(medications)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except InvalidId as ie:
        raise HTTPException(status_code=404, detail=str(ie))
    return {"message": "medicines added successfully", "ids": medication_ids}


@router.get("/extract-medicine-details", tags=["medications"])
def extract_medicine_details(text: str):
    try:
        extracted_details = MedicationService().analyze_text(text)
        medicine_details_response = MedicineDetailsExtractedPayload(
            **extracted_details
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    return medicine_details_response

