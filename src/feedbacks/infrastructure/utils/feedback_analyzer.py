import requests
from src.feedbacks.domain.enums.rating_enum import RatingEnum

API_URL = "https://r1w8d62lswudbn4r.us-east-1.aws.endpoints.huggingface.cloud"

def get_rating_enum(score: float):
    if score >= 0 and score <= 0.2:
        return RatingEnum.TOO_BAD
    elif score > 0.2 and score <= 0.4:
        return RatingEnum.BAD
    elif score > 0.4 and score <= 0.6:
        return RatingEnum.REGULAR
    elif score > 0.6 and score <= 0.8:
        return RatingEnum.GOOD
    elif score > 0.8 and score <= 1:
        return RatingEnum.EXCELLENT
    return RatingEnum.REGULAR

def analyze_sentiment(text: str):
    data = {
        "inputs": text,
        "parameters": {}
    }
    
    response = requests.post(API_URL, headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    }, json=data)
    
    if response.status_code == 200:
        result = response.json()
        score = result[0]['score']  
        return get_rating_enum(score)
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")