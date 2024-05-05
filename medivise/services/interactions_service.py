from medivise.utils.llm_response import get_json_response
from medivise.utils.mongo_client import db
from medivise.utils.llm import llm

class FoodInteractionsService:
    def __init__(self):
        self.db = db

    def get_food_interactions(self, medicine: str):
        prompt = f"""
        What different foods can't be consumed with {medicine}.
        If there are several foods with the same description, group them together with a comma as the "name" with just one description.
        Return a JSON array with the keys "name" is the name of the food, "description" is the reason why it can't be mixed. Do not return Markdown. 
        """
        response = llm.invoke(prompt)
        return get_json_response(response.content)
    