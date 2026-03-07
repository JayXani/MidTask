def normalize_status(payload: dict) -> list[dict]:
    size = max(len(v) for v in payload.values()) if len(payload) else 0
    status = []
    for i in range(size):

        status.append({
            "id": payload.get("id", [None])[i] if i < len(payload.get("id", [])) else None,
            "name": payload.get("name", [None])[i] if i < len(payload.get("name", [])) else None
        })
    return status