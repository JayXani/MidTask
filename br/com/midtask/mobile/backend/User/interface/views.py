from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from ..application.use_cases.create_user_use_case import CreateUserUseCase
from ..infra.repository import UserRepository
from .serializers import UserInputSerializer

class UserViewer(APIView):
    def post(self, request: Request):
        user_serializer = UserInputSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True) # Lanca erro no caso do dado ser invalido

        repository = UserRepository()
        use_case = CreateUserUseCase(repository)
        
        user_created = use_case.execute(user_serializer.validated_data) # Envio para o caso de uso um dicionario validado

        return Response({
            "teste": ""
        })
  