from ..models import Labels
from User.models import User
from ..domain.entities import LabelEntity
from django.db.models import Q #Mesma coisa do operador lógico OR

class LabelRepository():
    def create(self, labels_entities: list[LabelEntity], user_id: str):
        labels_created: list[LabelEntity] = []
        for label in labels_entities:
            label_inserted = Labels.objects.create(
                lab_id=label.id,
                lab_name=label.title,
                fk_lab_use_id=User.objects.get(use_id=user_id)
            )
            labels_created.append(
                LabelEntity(
                    id=label_inserted.lab_id,
                    title=label_inserted.lab_name,
                    created_at=label_inserted.created_at,
                    updated_at=label_inserted.updated_at
                )
            )
            
        return labels_created
    
    def find(self, id: str, user_id: str):
        label_founded = Labels.objects.get(
            fk_lab_use_id=user_id,
            lab_id=id
        )
        return [
            LabelEntity(
                id=label_founded.lab_id,
                title=label_founded.lab_name
            )
        ]

    def find_all(self, labels_entities: list[LabelEntity], user_id: str):
        query = Q()

        # A filtragem dos campos nós podemos usar o campo + __contains | __in (para array) etc
        for label in labels_entities:
            query |= Q(lab_id=label.id) | Q(lab_name__contains=label.title or "")

        labels_founded = Labels.objects.filter(
            query,
            fk_lab_use_id=user_id # Tem que ser separado pois é obrigatório e busca as labels desse usuário
        )

        labels_converted = [
            LabelEntity(
                id=label.lab_id,
                title=label.lab_name
            ) for label in labels_founded
        ]

        return labels_converted

    def delete(self, labels_entities: list[LabelEntity], user_id: str):
        query = Q()

        # A filtragem dos campos nós podemos usar o campo + __contains | __in (para array) etc
        for label in labels_entities:
            query |= Q(lab_id=label.id) | Q(lab_name=label.title or "")

        labels_deleted = Labels.objects.filter(
            query,
            fk_lab_use_id=user_id
        ).delete() # Ele filtra tudo da query e deleta
        return labels_deleted