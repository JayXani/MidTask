from ...infra.repository import LinksAssociatesRepository
from ...domain.entities import LinksEntity

def validate_to_update(link_entity: LinksEntity, user_id):
    if(not link_entity.link_reference or not link_entity.link_type):
        raise Exception("The link reference or link type cannot be empty !")

    repository = LinksAssociatesRepository()
    link_exists = repository.find(LinksEntity.id, user_id)

    if not link_exists: raise Exception(f"The link with id: {LinksEntity.id} not exists !")
    


