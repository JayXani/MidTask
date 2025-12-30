import re
from datetime import datetime
from ..entities import AlertEntity

def date_valid(date: str):
    regex = r"^(\d{4})-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]) ([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
    return re.match(regex, date)


def validate_dates_repeat(alert_entity: AlertEntity):
    repeat = alert_entity.repeat.lower().strip()
    alerts_repeat = [
        "month",
        "day",
        "null",
        "week",
        "semester",
        "trimester",
        "year"
    ]
    date_is_valid = date_valid(repeat)
    if(repeat not in alerts_repeat and not date_is_valid): raise Exception(
        f"Repeat date invalid, you can send: {",".join([r.upper() for r in alerts_repeat])} and DATE (EX: 2025-12-29 12:00:12)"
    )

    if(date_is_valid):
        date_converted = datetime.strptime(repeat, "%Y-%m-%d %H:%M:%S")
        if(date_converted <= datetime.now()): raise Exception("You can send only dates after now !")