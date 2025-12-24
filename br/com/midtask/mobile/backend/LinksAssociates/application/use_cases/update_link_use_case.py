from ...infra.repository import LinksAssociatesRepository
from ...domain.services.LinksPolicyService import validate_to_update
from ...domain.entities import LinksEntity

class UpdateLinksUseCase():
    def __init__(self):
        self.repository = LinksAssociatesRepository()

    def execute(self, link_id: str, links: dict, user_id: str): 
        if(not links): raise Exception("You cannot  send the object empty !")

        link_entity = LinksEntity(**links)
        link_entity.id = link_id
        
        validate_to_update(link_entity, user_id)

        link_updated = self.repository.update(link_entity, user_id)

        return link_updated