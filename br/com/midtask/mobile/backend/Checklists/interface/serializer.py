from rest_framework import serializers
from enum import Enum


class StatusChecklist(Enum):
    CONCLUDE= "CONCLUDE"
    PENDING = "PENDING"
    SCHEDULED="SCHEDULED"

class ChecklistInputSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        required=True
    )
    status = serializers.ChoiceField(
        choices=[ v.name for v in StatusChecklist],
        required=True
    )
    date = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        required=False,
    )
    description = serializers.CharField(
        max_length=200,
        required=True
    )
    
class ChecklistOutputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    date = serializers.DateTimeField(required=False)
    description = serializers.CharField(required=False)