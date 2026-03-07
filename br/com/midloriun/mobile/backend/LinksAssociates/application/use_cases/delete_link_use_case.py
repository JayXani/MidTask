from ...domain.entities import LinksEntity
from ...infra.repository import LinksAssociatesRepository

class DeleteLinkUseCase():
    def __init__(self):
        self.repository = LinksAssociatesRepository()

    def execute(self, links: dict, user_id: str):
        links_entities =  [
            LinksEntity(id=id)
            for id in links.get("id", [])
        ]
        links_exists = self.repository.findall(links_entities, user_id)
        if(not links_exists): return []

        links_deleted = self.repository.delete(links_entities, user_id)
        return links_deleted