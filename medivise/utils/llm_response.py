import json


def get_json_response(response):
    if response.startswith("```json"):
        response = response[7:]  # Remove "```json" from the beginning
    if response.endswith("```"):
        response = response[:-3]  # Remove "```" from the end
    return json.loads(response)
        
