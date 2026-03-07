from ..domain.entities import LinksEntity
from ..models import LinksAssociates
from User.models import User
from django.db.models import Q

class LinksAssociatesRepository():
    dict_keys = {
        "asc_name": "",
        "asc_link_reference": "",
        "asc_type": "",
        "asc_icon": "",
    }
    def create(self, link_entity: LinksEntity, user_id: str):

        link_created = LinksAssociates.objects.create(
            asc_id=link_entity.id,
            asc_name=link_entity.name,
            asc_link_reference=link_entity.link_reference,
            asc_type=link_entity.link_type,
            asc_icon=link_entity.icon,
            fk_asc_use_id = User.objects.get(use_id=user_id)
        )
        
        return LinksEntity(
            id=link_created.asc_id,
            name=link_created.asc_name,
            link_reference=link_created.asc_link_reference,
            link_type=link_created.asc_type
        )
    
    def find(self, id: str, user_id: str):
        links_founded = LinksAssociates.objects.get(
            asc_id=id,
            fk_asc_use_id=user_id
        )

        return LinksEntity(
            id=links_founded.asc_id,
            name=links_founded.asc_name,
            link_reference=links_founded.asc_link_reference,
            link_type=links_founded.asc_type,
            icon=links_founded.asc_icon
        )
    
    def update(self, link_entity: LinksEntity, user_id: str):
        if(link_entity.name): self.dict_keys["asc_name"] = link_entity.name
        if(link_entity.icon): self.dict_keys["asc_icon"] = link_entity.icon
        if(link_entity.link_reference): self.dict_keys["asc_link_reference"] = link_entity.link_reference
        if(link_entity.link_type): self.dict_keys["asc_type"] = link_entity.link_type


        LinksAssociates.objects.filter(
            asc_id=link_entity.id,
            fk_asc_use_id=user_id
        ).update(**self.dict_keys)
        
        link_updated = LinksAssociates.objects.get(asc_id=link_entity.id)
        return LinksEntity(
            id=link_updated.asc_id,
            name=link_updated.asc_name,
            link_reference=link_updated.asc_link_reference,
            link_type=link_updated.asc_type,
            icon=link_updated.asc_icon
        )
    
    def findall(self, links_entities: list[LinksEntity], user_id: str):
        query = Q()
        for link in links_entities:
            q_link = Q()

            if link.id:
                q_link |= Q(asc_id=link.id)

            if link.link_reference:
                q_link |= Q(asc_link_reference__icontains=link.link_reference)

            if link.name:
                q_link |= Q(asc_name__icontains=link.name)

            if link.link_type:
                q_link |= Q(asc_type__icontains=link.link_type)

            query |= q_link

        links_founded: list[LinksAssociates] = LinksAssociates.objects.filter(
            query,
            fk_asc_use_id=user_id
        )
        if not links_founded: return []
        return [
            LinksEntity(
                id=flink.asc_id,
                icon=flink.asc_icon,
                link_type=flink.asc_type,
                name=flink.asc_name,
                link_reference=flink.asc_link_reference
            )
            for flink in links_founded
        ]
    
    def delete(self, link_entity: list[LinksEntity], user_id: str):
        link_deleted = LinksAssociates.objects.filter(
            asc_id__in=[link.id for link in link_entity],
            fk_asc_use_id=user_id
        ).delete()

        return link_deleted