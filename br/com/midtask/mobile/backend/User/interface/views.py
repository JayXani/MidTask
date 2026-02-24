from ..application.use_cases.create_user_use_case import CreateUserUseCase
from ..application.use_cases.update_user_use_case import UpdateUserUseCase
from ..application.use_cases.get_user_use_case import GetUserUseCase
from ..application.use_cases.google_oauth_use_case import GoogleAuthUseCase
from ..infra.messages import format_response
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import (
    UserInputSerializer,
    UserUpdateSerializer,
    UserOutputSerializer,
    GoogleOauthSerializer
)

class UserViewer(APIView):
    def get_permissions(self):
        if(self.request.method == "POST"): # Rota pública somente para cadastro do usuário
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def post(self, request: Request):
        try:
            serializer = UserInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            use_case = CreateUserUseCase()
    
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
    
    def patch(self, request: Request):
        try: 
            serializer = UserUpdateSerializer(data=request.data, partial=True) #partial=True, indica que somente os dados com valores serao atualizados/serializados
            serializer.is_valid(raise_exception=True)
            
            use_case = UpdateUserUseCase()
            user_updated = use_case.execute(serializer.data, request.user.use_id)
            serializer_output = UserOutputSerializer(user_updated)

            return Response(format_response(
                success=True,
                message="Success ! User updated.",
                data=serializer_output.data
            ))
        
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Exception in update",
                err=e
            ))
    
    def get(self, request: Request):
        try:
            use_case = GetUserUseCase()
            user_founded = use_case.execute(request.user.use_id)
            output_serializer = UserOutputSerializer(user_founded)
            
            return Response(format_response(
                success=True,
                message="User founded !",
                data=output_serializer.data
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to get the user !",              
                err=e
            ))
    
    


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
                status=401
            )
        except Exception as e:
            return Response(
                format_response(
                    success=False,
                    err=e
                ),
                status=400
            )
        


class GoogleAuthenticationView(APIView):
    def post(self, request: Request):
        try:
            serializer = GoogleOauthSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            data_validated = serializer.validated_data
            use_case = GoogleAuthUseCase()
            user_token = use_case.execute(data_validated)
            
            return Response(
                format_response(
                    success=True,
                    message="Success ! Token provided.",
                    data=user_token
                )
            )
        except AuthenticationFailed as auth_err:
            return Response(
                format_response(
                    success=False,
                    message="Authentication failed!",
                    err=e
                ),
                status=401
            )

        except Exception as e:
            print(e)
            return Response(
                format_response(
                    success=False,
                    err=e
                ),
                status=400
            )