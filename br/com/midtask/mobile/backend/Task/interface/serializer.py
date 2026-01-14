from rest_framework import serializers
from enum import Enum


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
    status_id = serializers.ListField(required=True, child=serializers.UUIDField())
    alert_id = serializers.ListField(required=False, child=serializers.UUIDField())
    labels_id = serializers.ListField(required=False, child=serializers.UUIDField())
    links_id = serializers.ListField(required=False, child=serializers.UUIDField())


class TaskOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    title = serializers.CharField()
    description = serializers.CharField()
    recurrence = serializers.CharField()
    recurrence_end_in = serializers.DateTimeField()
    expected_conclude_in = serializers.CharField()
    conclude_at = serializers.CharField()
    background = serializers.CharField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()


class TaskListInputSerializer(serializers.Serializer):
    id=serializers.ListField(
        child=serializers.UUIDField()
    )