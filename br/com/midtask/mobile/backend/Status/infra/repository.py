from ..models import Status
from ..domain.entities import StatusEntity
from User.models import User
from django.db.models import Q

class StatusRepository():
    def create(self, status_entity: list[StatusEntity], user_id: str):
        status_created = [
            Status.objects.create(
                sta_id=status.id,
                sta_name=status.name,
                fk_sta_use_id=User.objects.get(use_id=user_id)
            ) for status in status_entity
        ]

        return [
            StatusEntity(
                id=status.sta_id,
                name=status.sta_name
            ) for status in status_created
        ]
    
    def findall(self, status_entity: list[StatusEntity], user_id: str):
        query = Q()
        for status in status_entity:
            if(status.id): query |= Q(sta_id=status.id)
            if(status.name): query |=Q(sta_name__contains=status.name or "")

        status_founded = Status.objects.filter(
            query,
            fk_sta_use_id=user_id
        )

        if not status_founded: return []
        return [
            StatusEntity(
                id=status.sta_id,
                name=status.sta_name
            ) for status in status_founded
        ]
    

    def delete(self, status_entity: list[StatusEntity], user_id: str):
        status_deleted = Status.objects.filter(
            sta_id__in=[status.id for status in status_entity],
            fk_sta_use_id=user_id
        ).delete()

        if not status_deleted: return []
        return status_deleted