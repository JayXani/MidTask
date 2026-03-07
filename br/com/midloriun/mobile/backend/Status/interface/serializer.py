from rest_framework import serializers

class StatusInputSerializer(serializers.Serializer):
    status=serializers.ListField(
        child=serializers.CharField(max_length=10),
        required=True
    )


class StatusOutputSerializer(serializers.Serializer):
    id=serializers.UUIDField(required=False)
    name=serializers.CharField(required=False)


class StatusListInputSerializer(serializers.Serializer):
    status=serializers.DictField(
        child=serializers.ListField(),
        required=False
    )