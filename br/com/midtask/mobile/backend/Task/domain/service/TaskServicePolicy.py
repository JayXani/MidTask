from Alerts.infra.repository import AlertsRepository
from Alerts.domain.entities import AlertEntity

from Labels.infra.repository import LabelRepository
from Labels.domain.entities import LabelEntity

from LinksAssociates.infra.repository import LinksAssociatesRepository
from LinksAssociates.domain.entities import LinksEntity

from Status.infra.repository import StatusRepository
from Status.domain.entities import StatusEntity

class TaskServicePolicy():
    def __init__(self, user_id: str):
        self.user_id=user_id 
        self.alert_repository = AlertsRepository()
        self.status_repository = StatusRepository()
        self.links_repository = LinksAssociatesRepository()
        self.labels_repository = LabelRepository()

    def alerts_exists(self, alerts_id: list[str]):
        alerts_exists = self.alert_repository.findall(
            [AlertEntity(id=v) for v in alerts_id],
            self.user_id
        )
        
        if(len(alerts_exists) != len(alerts_id)): raise Exception("You sended the alerts id invalid ! Verify the ids.")
        if(not len(alerts_exists)): raise Exception("Alerts not found !")

    def labels_exists(self, labels_id: list[str]):
        labels_exists = self.labels_repository.find_all(
            [LabelEntity(id=v) for v in labels_id],
            self.user_id
        )

        if(len(labels_exists) != len(labels_id)): raise Exception("You sended the labels id invalid ! Verify the ids.")
        if(not len(labels_exists)): raise Exception("Labels not found !")

    def status_exists(self, status_id: list[str]):
        status_exists = self.status_repository.findall(
            [StatusEntity(id=v) for v in status_id],
            self.user_id
        )

        if(len(status_exists) != len(status_id)): raise Exception("You sended the status id invalid ! Verify the ids.")
        if(not len(status_exists)): raise Exception("Status not found !")

    def links_exists(self, links_id: list[str]):
        links_exists = self.links_repository.findall(
            [LinksAssociatesRepository(id=v) for v in links_id],
            self.user_id
        )

        if(len(links_exists) != len(links_id)): raise Exception("You sended the Links id invalid ! Verify the ids.")
        if(not len(links_exists)): raise Exception("Links not found !")

