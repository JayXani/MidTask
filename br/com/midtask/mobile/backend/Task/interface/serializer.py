from rest_framework import serializers
from enum import Enum

class TaskStatusEnum(Enum):
    STOPPED = "Stopped"
    RUNNING = "Running"
    CONCLUDE = "Conclude"
    IN_BACKLOG="Backlog"

class TaskInputSerializer(serializers.Serializer):
    id=serializers.UUIDField(required=False)
    title=serializers.CharField(
        max_length=40, 
        required=True
    )
    description=serializers.CharField(
        required=True
    )
