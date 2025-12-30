from ..domain.entities import AlertEntity
from ..models import Alerts
from User.models import User
from django.db.models import Q

class AlertsRepository():
    def create(self, alert_entity: AlertEntity, user_id: str):
        alert_created = Alerts.objects.create(
            ale_id=alert_entity.id,
            ale_repeat=alert_entity.repeat,
            ale_date=alert_entity.date,
            fk_ale_use_id=User.objects.get(use_id=user_id)
        )

        return AlertEntity(
            id=alert_created.ale_id,
            date=alert_created.ale_date,
            repeat=alert_created.ale_repeat,
        )
    
    def findall(self, alerts_entities: list[AlertEntity], user_id: str):
        query = Q()
        for alert in alerts_entities:
            query |= Q(ale_id=alert.id) | Q(ale_date=alert.date) | Q(ale_repeat=alert.repeat)
            query |= Q(ale_date__date=alert.date)

        alerts_filtered = Alerts.objects.filter(
            query,
            fk_ale_use_id=user_id
        )
        
        return [
            AlertEntity(
                id=alert.ale_id,
                date=alert.ale_date,
                repeat=alert.ale_repeat
            ) for alert in alerts_filtered
        ]