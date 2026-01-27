from rest_framework import serializers
from enum import Enum
from Alerts.interface.serializer import OutputSerializer
from Status.interface.serializer import StatusOutputSerializer
from Labels.interfaces.serializers import LabelOutputSerializer


class RecurrenceEnum(Enum):
    MONTH = "month"
    WEEK = "week"
    DAY = "day"
    NULL = None


class TaskInputSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    title = serializers.CharField(max_length=40, required=True)
    description = serializers.CharField(required=True)
    recurrence = serializers.ChoiceField(
        choices=[v.name for v in RecurrenceEnum], required=False
    )
    recurrence_end_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False
    )
    expected_conclude_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False
    )
    conclude_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    background = serializers.CharField(required=True, max_length=10)
    status = serializers.ListField(required=True, child=serializers.UUIDField())
    alerts = serializers.ListField(required=False, child=serializers.UUIDField())
    labels = serializers.ListField(required=False, child=serializers.UUIDField())
    links = serializers.ListField(required=False, child=serializers.UUIDField())


class TaskOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    title = serializers.CharField()
    description = serializers.CharField()
    recurrence = serializers.CharField()
    recurrence_end_in = serializers.DateTimeField()
    expected_conclude_in = serializers.CharField()
    alerts = OutputSerializer(many=True)
    status = StatusOutputSerializer()
    labels = LabelOutputSerializer(many=True)
    conclude_at = serializers.CharField()
    background = serializers.CharField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()


class TaskListInputSerializer(serializers.Serializer):
    id = serializers.ListField(
        child=serializers.UUIDField(),
        required=False
    )
    title = serializers.ListField(child=serializers.CharField(), required=False)
    recurrence = serializers.ListField(child=serializers.CharField(), required=False)
    recurrence_end_in = serializers.ListField(child=serializers.CharField(), required=False)
    expected_conclude_in = serializers.ListField(child=serializers.CharField(), required=False)
    background = serializers.ListField(child=serializers.CharField(), required=False)
    conclude_at = serializers.ListField(child=serializers.CharField(), required=False)
    

class TaskUpdateInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=40, required=False)
    description = serializers.CharField(required=False)
    recurrence = serializers.ChoiceField(
        choices=[v.name for v in RecurrenceEnum], required=False
    )
    recurrence_end_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False
    )
    expected_conclude_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False
    )
    conclude_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    background = serializers.CharField(required=False, max_length=10)
    status = serializers.ListField(required=False, child=serializers.UUIDField())
    alerts = serializers.ListField(required=False, child=serializers.UUIDField())
    labels = serializers.ListField(required=False, child=serializers.UUIDField())
    links = serializers.ListField(required=False, child=serializers.UUIDField())
