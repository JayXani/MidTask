from ...infra.repository import AlertsRepository
from ...domain.entities import AlertEntity
from ...domain.service.AlertsPolicy import normalize_payload

# ADICIONAR NA POLICY A VERIFICACAO PARA REMOVER O ID DO ALERTA NAS TASKS
class DeleteAlertsUseCase():
    def __init__(self):
        self.repository = AlertsRepository()

    def execute(self, alerts_ids: dict, user_id: str):
        alert_entities = normalize_payload(alerts_ids)
        alerts_exists = self.repository.findall(alert_entities, user_id)

        if(not alerts_exists): return []

        alerts_deleted = self.repository.delete(alert_entities, user_id)
        return alerts_deleted