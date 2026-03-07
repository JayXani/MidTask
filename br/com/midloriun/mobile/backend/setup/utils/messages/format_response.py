
def format_response(success: bool, message: str = "", data=None):
    response = {
        "success": success,
        "data": data if data is not None else {},
        "messages": [message]
    }

    return response
