from rest_framework import serializers

class AlertInputSerializer(serializers.Serializer):
    id=serializers.UUIDField(
        required=False,
    )
    date=serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        required=True,
        allow_null=False
    )
    repeat=serializers.CharField(
        required=True,
        allow_null=False
    )
    name=serializers.CharField(
        required=True
    )
class AlertInputUpdateSerializer(serializers.Serializer):
    id=serializers.UUIDField(
        required=False,
    )
    date=serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        required=False,
        allow_null=False
    )
    repeat=serializers.CharField(
        required=False,
        allow_null=False
    )
    name=serializers.CharField(
        required=False
    )

class AlertsListInputSerializer(serializers.Serializer):
    id=serializers.ListField(
        child=serializers.CharField(),
        required=False 
    )
    date=serializers.ListField(
        child=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S"),
        required=False
    )
    repeat=serializers.ListField(
        child=serializers.DateField(format="%Y-%m-%d"),
        required=False
    )
    name=serializers.ListField(
        child=serializers.CharField(),
        required=False
    )


class OutputSerializer(serializers.Serializer):
    id=serializers.UUIDField()
    date=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    repeat=serializers.CharField()
    name=serializers.CharField()