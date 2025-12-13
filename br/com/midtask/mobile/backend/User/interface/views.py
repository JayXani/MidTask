from ..application.use_cases.create_user_use_case import CreateUserUseCase
from ..infra.messages import format_response
from ..infra.repository import UserRepository
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (
    UserInputSerializer,
    UserOutputSerializer
)

class UserViewer(APIView):
    def get_permissions(self):
        if(self.request.method == "POST"):
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def post(self, request: Request):
        try:
            serializer = UserInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            repository = UserRepository()
            use_case = CreateUserUseCase(repository)
    
            # validated_data vem convertido e tipado
            user_created = use_case.execute(serializer.validated_data)
            return Response(format_response(
                success=True, 
                data={
                    "id": user_created.id,
                    "email": user_created.email
                },
                message="Sucesso ! Usuário cadastrado com sucesso"
            ))

        except ValidationError as vError:
            return Response(format_response(False, err=vError.detail))
        
        except Exception as e: 
            return Response(format_response(False, err=e))

    def get(self, request: Request):
        try: 
            repository = UserRepository()
            users = repository.find_all()
            serializer = UserOutputSerializer(users, many=True)
            
            return Response(format_response(
                success=True,
                message="Usuários retornados.",
                data=serializer.data
            ))
        except Exception as e:

            return Response(
                format_response(
                    success=False,
                    err=e
                )
            )
        

# Otimizando o método de autenticacao e padronizando o retorno dos erros
class Authentication(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            return Response(
                format_response(
                    success=True,
                    message="Login success !",
                    data=serializer.validated_data
                )
            )

        except AuthenticationFailed as e:
            return Response(
                format_response(
                    success=False,
                    message="Authentication failed!",
                    err=e
                ),
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            return Response(
                format_response(
                    success=False,
                    err=e
                )
            )