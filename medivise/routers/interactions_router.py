from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

from medivise.services.interactions_service import FoodInteractionsService
from medivise.services.medication_service import MedicationService
from medivise.services.report_service import ReportService

router = APIRouter()


@router.get("/interactions/medication", tags=["interactions"])
def get_interactions_between_medications(medicine_a: str, medicine_b: str):
    return MedicationService().check_interactions(medicine_a, medicine_b)


@router.get("/interactions/food", tags=["interactions"])
def get_interactions_with_food(medicine: str):
    return FoodInteractionsService().get_food_interactions(medicine)


@router.get("/user/{user_id}/medications/pdf", tags=["interactions"])
def get_interactions_pdf(user_id: str):

    pdf_buffer = ReportService().generate_medication_report(user_id)
    # Return the PDF file as a response
    return Response(content=pdf_buffer.read(), media_type='application/pdf', headers={"Content-Disposition": "attachment; filename=medications.pdf"})

