from ...infra.repository import LinksAssociatesRepository
from ...domain.entities import LinksEntity

class FindUniqueLinkUseCase():
    def __init__(self):
        self.repository = LinksAssociatesRepository()

    def execute(self, link_id: str, user_id): 
        links_founded = self.repository.find(link_id, user_id)
        if(not links_founded): return []

        return [links_founded]