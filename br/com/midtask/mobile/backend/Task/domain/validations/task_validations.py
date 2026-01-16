import re
from ..entities import TaskEntity
from Alerts.infra.repository import AlertsRepository
from Alerts.domain.entities import AlertEntity

from Labels.infra.repository import LabelRepository
from Labels.domain.entities import LabelEntity

from LinksAssociates.infra.repository import LinksAssociatesRepository
from LinksAssociates.domain.entities import LinksEntity

from Status.infra.repository import StatusRepository
from Status.domain.entities import StatusEntity


def alerts_exists(alerts_id: list[str], user_id: str):
    alert_repository =  AlertsRepository()
    alerts_exists = alert_repository.findall(
        [AlertEntity(id=v) for v in alerts_id],
        user_id
    )
    
    if(len(alerts_exists) != len(alerts_id)): raise Exception("You sended the alerts id invalid ! Verify the ids.")
    if(not len(alerts_exists)): raise Exception("Alerts not found !")

def labels_exists(labels_id: list[str], user_id: str):
    labels_repository =  LabelRepository()
    labels_exists = labels_repository.find_all(
        [LabelEntity(id=v) for v in labels_id],
        user_id
    )

    if(len(labels_exists) != len(labels_id)): raise Exception("You sended the labels id invalid ! Verify the ids.")
    if(not len(labels_exists)): raise Exception("Labels not found !")

def status_exists(status_id: list[str], user_id: str):
    status_repository =  StatusRepository()
    status_exists = status_repository.findall(
        [StatusEntity(id=v) for v in status_id],
        user_id
    )

    if(len(status_exists) != len(status_id)): raise Exception("You sended the status id invalid ! Verify the ids.")
    if(not len(status_exists)): raise Exception("Status not found !")

def links_exists(links_id: list[str], user_id: str):
    links_repository =  LinksAssociatesRepository()
    links_exists = links_repository.findall(
        [LinksEntity(id=v) for v in links_id],
        user_id
    )

    if(len(links_exists) != len(links_id)): raise Exception("You sended the Links id invalid ! Verify the ids.")
    if(not len(links_exists)): raise Exception("Links not found !")

def date_valid(date: str):
    regex = r"^(\d{4})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]) ([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
    return re.match(regex, date)


def normalize_payload(payload: dict):
    size = max(len(v) for v in payload.values())
    data = []
    for i in range(size):
        data.append(TaskEntity(
            id=payload.get("id", [None])[i] if i < len(payload.get("id", "")) else None,
            title=payload.get("title", [None])[i] if i < len(payload.get("title", "")) else None,
            recurrence=payload.get("recurrence", [None])[i] if i < len(payload.get("recurrence", "")) else None,
            recurrence_end_in=payload.get("recurrence_end_in", [None])[i] if i < len(payload.get("recurrence_end_in", "")) else None,
            expected_conclude_in=payload.get("expected_conclude_in", [None])[i] if i < len(payload.get("expected_conclude_in", "")) else None,
            conclude_at=payload.get("conclude_at", [None])[i] if i < len(payload.get("conclude_at", "")) else None,
            background=payload.get("background", [None])[i] if i < len(payload.get("background", "")) else None
        ))

    return data