from uuid import uuid4
from ...infra.repository import UserRepository
from ...Domain.entities import UserEntity
from Notifications.infra.jobs.send_email import send_welcome_email_task

class CreateUserUseCase:
    def __init__(self):
        self.user_repository = UserRepository()

    def execute(self, data: dict) -> UserEntity:
        user = UserEntity(
            id=uuid4(),
            **data
        )

        user_created = self.user_repository.save(user)
        if user_created:
            send_welcome_email_task.delay(
                {
                    "name": user_created.name,
                    "date_start": user_created.created_at.strftime("%d/%m/%Y"),
                    "email": user_created.email,
                },
                user_created.email
            )


        return user_created