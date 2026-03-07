from ...infra.repository import AlertsRepository
from ...domain.entities import AlertEntity

class FindUniqueAlertUseCase():
    def __init__(self): 
        self.repository = AlertsRepository()

    def execute(self, alert_id: str, user_id: str):
        alert_founded = self.repository.find(AlertEntity(id=alert_id), user_id)
        return alert_founded