from ..domain.entities import AlertEntity
from ..models import Alerts
from User.models import User
from django.db.models import Q

class AlertsRepository():
    dict_keys = {}
    def create(self, alert_entity: AlertEntity, user_id: str):
        alert_created = Alerts.objects.create(
            ale_id=alert_entity.id,
            ale_repeat=alert_entity.repeat,
            ale_date=alert_entity.date,
            ale_name=alert_entity.name,
            fk_ale_use_id=User.objects.get(use_id=user_id)
        )

        return AlertEntity(
            id=alert_created.ale_id,
            date=alert_created.ale_date,
            repeat=alert_created.ale_repeat,
            name=alert_created.ale_name,
        )
    
    def findall(self, alerts_entities: list[AlertEntity], user_id: str):
        query = Q()
        for alert in alerts_entities:
            if alert.id: query |= Q(ale_id=alert.id)
            if alert.date: query |= Q(ale_date=alert.date)
            if alert.repeat: query |= Q(ale_repeat=alert.repeat)
            if alert.date: query |= Q(ale_date__date=alert.date)
            if alert.name: query |= Q(ale_name__in=alert.name)
   

        alerts_filtered = Alerts.objects.filter(
            query,
            fk_ale_use_id=user_id
        )
        return [
            AlertEntity(
                id=alert.ale_id,
                date=alert.ale_date,
                repeat=alert.ale_repeat,
                name=alert.ale_name
            ) for alert in alerts_filtered
        ]
    
    def find(self, alert_entity: AlertEntity, user_id: str):
        alert_founded = Alerts.objects.get(
            ale_id=alert_entity.id,
            fk_ale_use_id=user_id
        )
        if not alert_founded: return []
        return [
            AlertEntity(
                id=alert_founded.ale_id,
                date=alert_founded.ale_date,
                repeat=alert_founded.ale_repeat,
                name=alert_founded.ale_name
            )
        ]
    
    def update(self, alert_entity: AlertEntity, user_id: str):
        if alert_entity.date: self.dict_keys["ale_date"] = alert_entity.date
        if alert_entity.repeat: self.dict_keys["ale_repeat"] = alert_entity.repeat
        if alert_entity.name: self.dict_keys["ale_name"] = alert_entity.name
        
        Alerts.objects.filter(
            ale_id=alert_entity.id,
            fk_ale_use_id=user_id
        ).update(**self.dict_keys)

        alert_founded = Alerts.objects.get(
            ale_id=alert_entity.id,
            fk_ale_use_id=user_id
        )
        return [
            AlertEntity(
                id=alert_founded.ale_id,
                date=alert_founded.ale_date,
                repeat=alert_founded.ale_repeat,
                name=alert_founded.ale_name
            )
        ]
    
    def delete(self, alert_entity: list[AlertEntity], user_id: str):
        alerts_deleted = Alerts.objects.filter(
            ale_id__in=[alert.id for alert in alert_entity],
            fk_ale_use_id=user_id
        ).delete()

        return alerts_deleted