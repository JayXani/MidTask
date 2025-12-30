from rest_framework.exceptions import ValidationError
from rest_framework.utils.serializer_helpers import ReturnDict
from django.db.utils import IntegrityError

def format_response(success: bool, message: str = "", data=None, err: Exception | None = None):
    if data is None:
        data = {}

    error = {
        "code": 400,
        "details": None
    }

    response = {
        "success": success,
        "data": data,
    }

    if success:
        response["message"] = message

    if err:
        match err:
            case ValidationError(): # Valida pelo objeto da classe
                error["details"] = err.detail
     
            case IntegrityError():
                error["details"] = {
                    "unique_key_violated": str(err.args)
                }
            case Exception():
                error["details"] = {
                    "default": str(err)
                }

            case ReturnDict():
                error["details"] = err


        if error["details"] is not None:
            response["error"] = error

    return response
