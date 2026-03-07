import re
from .errors_code import ErrorsCode
from rest_framework.response import Response
from rest_framework.views import exception_handler


def get_error_data(name) -> dict:

    error = ErrorsCode.get(name)
    if error: return error
    return ErrorsCode.get("ERROR_NOT_MAPPED", '')


def exception_errors(exc, context):

    response = exception_handler(exc, context)
    reference_errors = []
    descriptions = []
    if hasattr(exc, "get_codes"):
        codes = exc.get_codes()
        details = exc.detail
        if isinstance(codes, dict):

            for field in codes:
                for i, code in enumerate(codes[field]):
                    mapped = ErrorsCode.get(code.upper(), ErrorsCode.get("ERROR_NOT_MAPPED", ''))
                    reference_errors.append(mapped.get('code', ''))
                    descriptions.append(f"{str(field).upper()}: {str(details[field][i])}")

        elif isinstance(codes, list):
            for i, code in enumerate(codes):

                mapped = ErrorsCode.get(code.upper(), ErrorsCode.get("ERROR_NOT_MAPPED", ''))
                reference_errors.append(mapped.get('code', ''))
                descriptions.append(str(exc.detail[i]))

        elif isinstance(codes, str): 
            mapped = ErrorsCode.get(codes.upper(), ErrorsCode.get('ERROR_NOT_MAPPED', {}))
            
            reference_errors.append(mapped.get("code", ""))
            descriptions.append(str(exc.detail))


        return Response(
            {
                "success": False,
                "error": {
                    "unique_id": ".".join([f"{x[1:]}".replace("-", "") for x in reference_errors]),
                    "references": reference_errors, 
                    "messages": descriptions
                }
            },
            status=response.status_code if response else 400,
        )

    error_data= get_error_data(name = type(exc).__name__.upper())
    match = re.search(r'Key \((.*?)\)', str(exc)) #Captura o campo que gerou erro
    field = match.group(1) if match else None

    return Response({
        "success": False,
        "error": {
            "unique_id": ".".join([f"{x[1:]}".replace("-", "") for x in [error_data.get("code", "")]]),
            "references": [error_data.get("code", "")],
            "messages": [error_data.get("generic_text", "")],
            "field_error": field
        }
    })
    
  