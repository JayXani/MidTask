from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from ..application.use_cases.create_user_use_case import CreateUserUseCase
from ..infra.repository import UserRepository
from .serializers import UserInputSerializer
from rest_framework.serializers import ValidationError
from ..infra.messages import format_response

class UserViewer(APIView):
    def post(self, request: Request):
        try:
            serializer = UserInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            repository = UserRepository()
            use_case = CreateUserUseCase(repository)

            # validated_data vem convertido e tipado
            user_created = use_case.execute(serializer.validated_data)
            output = UserInputSerializer(user_created)

            return Response(format_response(True, data=output.data))

        except ValidationError as vError:
            return Response(format_response(False, err=vError.detail))
        
        except Exception as e: 
            return Response(format_response(False, err=e))

    