from ...domain.entities import AlertEntity
from ...domain.service.AlertsPolicy import (
    validate_dates_repeat
)
from ...infra.repository import AlertsRepository


class CreateAlertsUseCase():
    def __init__(self):
        self.repository = AlertsRepository()

    def execute(self, alert: dict, user_id: str):
        alert_entity = AlertEntity(**alert)
        validate_dates_repeat(alert_entity)
    
        alert_created = self.repository.create(
            alert_entity,
            user_id
        )
        return [alert_created]