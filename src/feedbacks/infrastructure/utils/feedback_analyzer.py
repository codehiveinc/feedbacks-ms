from transformers import BertTokenizer, BertForSequenceClassification
import torch

from src.feedbacks.domain.enums.rating_enum import RatingEnum

tokenizer = BertTokenizer.from_pretrained(
    "nlptown/bert-base-multilingual-uncased-sentiment"
)
model = BertForSequenceClassification.from_pretrained(
    "nlptown/bert-base-multilingual-uncased-sentiment"
)

num_classes = 5
sentiment_classes = ["Too Bad", "Bad", "Neutral", "Good", "Excellent"]


def get_rating_enum(result: str):
    if result == "Too Bad":
        return RatingEnum.TOO_BAD
    if result == "Bad":
        return RatingEnum.BAD
    if result == "Neutral":
        return RatingEnum.REGULAR
    if result == "Good":
        return RatingEnum.GOOD
    if result == "Excellent":
        return RatingEnum.EXCELLENT
    return RatingEnum.REGULAR


def analyze_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    sentiment_result = torch.argmax(logits, dim=1).item()

    result = sentiment_classes[sentiment_result]

    return get_rating_enum(result)
