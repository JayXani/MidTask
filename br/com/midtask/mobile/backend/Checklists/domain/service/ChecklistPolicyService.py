from ..entities import ChecklistEntity
from datetime import datetime, timedelta

class CheckListPolicyService():
    def __init__(self, checklist: ChecklistEntity):
        self.entity = checklist

    def validate_to_create(self):
        date_now = datetime.now()
        date_entity = self.entity.date

        if(self.entity.date.time() < date_now.time() and (date_entity.date() >= date_now.date())): raise Exception("The date cannot be less than now !")
        if(self.entity.status.upper() == "SCHEDULED"): self.validate_date_scheduling(date_now)


    def validate_date_scheduling(self, date_now: datetime):
        if(not self.entity.date): raise Exception("You choose the SCHEDULED status, but you din't sended the date of scheduling")
        if(self.entity.date.time() < (date_now + timedelta(hours=1)).time()): raise Exception("You can scheduling only after 1 hour of the date now !")
