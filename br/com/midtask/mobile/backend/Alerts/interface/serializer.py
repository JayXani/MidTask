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

class OutputSerializer(serializers.Serializer):
    id=serializers.UUIDField()
    date=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    repeat=serializers.CharField()