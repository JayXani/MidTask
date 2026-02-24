from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings

class GoogleAuthUseCase():
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, user_data: dict):
        try:
            user_google_exists = id_token.verify_oauth2_token(
                user_data.get("google_id", ""),
                requests.Request(),
                settings.GOOGLE_CLIENT_ID
            )
            #Na hora da busca, o tipo de login tem que ser único para que a query filtre de acordo com o tipo de login
            user_entity = UserEntity(
                login_type="google",
                google_id=user_google_exists.get("sub", "") # Google ID retornado pelo google
            )

            if user_google_exists:
                user_entity.ip_address = user_data.get("ip_address", "")
                user_entity.email = user_data.get("use_email", "")
                user = self.repository.find(user_entity)
                if not user: 
                    user_entity.name = user_google_exists.get("name", "")
                    user_entity.avatar = user_google_exists.get("picture", "")
                    user_created = self.repository.save(user_entity)

                    if not user_created: raise Exception("Error to generate user and token!")

                    refresh_token = RefreshToken.for_user(user_created)

                    return {
                        "access": str(refresh_token.access_token),
                        "refresh": str(refresh_token)
                    }
                
                # Se o usuário já existir, permitimos que ele faca login pelo basic ou pelo google
                # Mas nao é permitido um usuário logado com o google fazer login pelo basic
                if user and not user.google_id:
                    user_updated = self.repository.assign_google_user(user_entity)
                    if user_updated: 
                        print(user_updated)
                        refresh_token = RefreshToken.for_user(user_updated)

                        return {
                            "access": str(refresh_token.access_token),
                            "refresh": str(refresh_token)
                        }
                    
            raise Exception("Google client not available !")
        except Exception as e:
            print(e)
            raise Exception("Token Not provided !")
        