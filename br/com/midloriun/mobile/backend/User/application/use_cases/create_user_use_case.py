from uuid import uuid4
from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity
from Notifications.infra.jobs.send_email import send_emails

class CreateUserUseCase:
    def __init__(self):
        self.user_repository = UserRepository()

    def execute(self, data: dict) -> UserEntity:
        user = UserEntity(
            id=uuid4(),
            login_type="basic", #Todo login realizado pela API de user, deve ser do tipo basic
            **data
        )

        user_created = self.user_repository.save(user)
        user_entity = UserEntity(
            id=user_created.use_id,
            name=user_created.use_name,
            status=user_created.use_status,
            email=user_created.use_email,
            phone=user_created.use_phone,
            login_type=user_created.use_login_type,
            ip_address=user_created.use_ip_address,
            created_at=user_created.created_at,
            updated_at=user_created.updated_at,
        )
        if user_created:
            send_emails.delay(
                "emails/welcome.html",
                {
                    "name": user_entity.name,
                    "date_start": user_entity.created_at.strftime("%d/%m/%Y"),
                    "subject":"Bem-vindo à plataforma 🎉", 
                    "email": user_entity.email,
                },
                user_entity.email
            )


        return user_entity