from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from ..application.use_cases.create_user_use_case import CreateUserUseCase

class UserViewer(APIView):
    def post(self, request: Request):
        use_case = CreateUserUseCase(request.data)
    
  