from rest_framework.exceptions import APIException
from rest_framework import status


class CategoryAlreadyExists(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "A category with this name already exists."
    default_code = "category_exists"


class CardNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Card not found."
    default_code = "card_not_exists"
