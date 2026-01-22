from ..entities import ChecklistEntity

def normalize_payload(payload: dict):
    size = max(len(v) for v in payload.values()) if payload else 0
    data = []
    for i in range(size):
        data.append(ChecklistEntity(
            id=payload.get("id", [None])[i] if i < len(payload.get("id", "")) else None,
            date=payload.get("date", [None])[i] if i < len(payload.get("date", "")) else None,
            description=payload.get("description", [None])[i] if i < len(payload.get("description", "")) else None,
            name=payload.get("name", [None])[i] if i < len(payload.get("name", "")) else None,
            status=payload.get("status", [None])[i] if i < len(payload.get("status", "")) else None,
            task_id=payload.get("task_id", [None])[i] if i < len(payload.get("task_id", "")) else None,
        ))

    return data