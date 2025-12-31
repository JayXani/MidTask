from ...infra.repository import AlertsRepository
from ...domain.entities import AlertEntity
from ...domain.service.AlertsPolicy import (validate_dates_repeat)

class UpdateAlertsUseCase():
    def __init__(self):
        self.repository = AlertsRepository()
    
    def execute(self, alert: dict, user_id: str):
        alert_entity = AlertEntity(**alert)
        if(alert_entity.repeat): validate_dates_repeat(alert_entity)

        alert_updated = self.repository.update(alert_entity, user_id)
        if not alert_updated: return []

        return alert_updated