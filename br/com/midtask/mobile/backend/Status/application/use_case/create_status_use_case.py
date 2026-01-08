from ...infra.repository import StatusRepository
from ...domain.entities import StatusEntity


class CreateStatusUseCase:
    def __init__(self):
        self.repository = StatusRepository()

    def execute(self, status: dict, user_id: str):
        status_default = ["CONCLUDE", "PENDING", "CANCELED"]
        exists_status_default = list(filter(lambda x: x.upper() in status_default, status.get("status", [])))

        if len(exists_status_default):
            raise Exception(
                f"The {",".join(status_default)} status is created automatically, you don't created."
            )
        status["status"].extend(status_default)

        status_entities = [StatusEntity(name=s) for s in status.get("status", [])]

        status_created = self.repository.create(status_entities, user_id)
        return status_created
