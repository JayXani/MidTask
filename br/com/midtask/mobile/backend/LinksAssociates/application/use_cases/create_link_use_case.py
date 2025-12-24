from ...infra.repository import LinksAssociatesRepository
from ...domain.entities import LinksEntity

class CreateLinksUseCase():
    def __init__(self):
        self.repository = LinksAssociatesRepository()

    def execute(self, links: dict, user_id: str):
        link_entity = LinksEntity(**links)
        link_inserted = self.repository.create(link_entity, user_id)

        return link_inserted