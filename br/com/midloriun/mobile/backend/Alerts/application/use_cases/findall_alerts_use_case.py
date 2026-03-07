from ...infra.repository import AlertsRepository
from ...domain.service.AlertsPolicy import normalize_payload

class FindAllAlertsUseCase():
    def __init__(self):
        self.repository = AlertsRepository()
    
    def execute(self, alerts: dict, user_id: str):
        alerts_normalized = normalize_payload(alerts)
        alerts_founded = self.repository.findall(alerts_normalized, user_id)

        if(not alerts_founded): return []
        return alerts_founded