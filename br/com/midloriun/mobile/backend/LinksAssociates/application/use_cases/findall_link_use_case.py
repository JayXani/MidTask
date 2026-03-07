from ...infra.repository import LinksAssociatesRepository
from ...domain.entities import LinksEntity


def normalize_links_payload(payload: dict) -> list[dict]:
    size = max(len(v) for v in payload.values())

    links = []
    for i in range(size):

        links.append({
            "id": payload.get("id", [None])[i] if i < len(payload.get("id", [])) else None,
            "name": payload.get("name", [None])[i] if i < len(payload.get("name", [])) else None,
            "link_reference": payload.get("link_reference", [None])[i] if i < len(payload.get("link_reference", [])) else None,
            "link_type": payload.get("link_type", [None])[i] if i < len(payload.get("link_type", [])) else None,
        })
    return links


class FindAllLinksUseCase():
    def __init__(self): 
        self.repository = LinksAssociatesRepository()

    def execute(self, links: dict, user_id: str):
        links_filtered = normalize_links_payload(links)
        links_entities = [
            LinksEntity(
                id=link.get("id", ''),
                name= link.get("name", ''),
                link_reference= link.get("link_reference",''),
                link_type= link.get("link_type", ''),
            )
            for link in links_filtered
        ]
        links_founded = self.repository.findall(links_entities, user_id)
        return links_founded