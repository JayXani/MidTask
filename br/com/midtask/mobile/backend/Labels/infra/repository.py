from ..models import Labels
from User.models import User
from ..domain.entities import LabelEntity

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

