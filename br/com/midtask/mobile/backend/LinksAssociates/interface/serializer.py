from rest_framework import serializers
from enum import Enum

class LinkTypes(Enum):
    HTTP='http',
    MOBILE='mobile'

class LinksInputSerializer(serializers.Serializer):
    id=serializers.UUIDField(required=False)
    name=serializers.CharField(required=False)
    link_reference=serializers.CharField(required=True, allow_null=False)
    link_type=serializers.ChoiceField(
        choices=[l.name for l in LinkTypes],
        required=True
    )
    icon=serializers.CharField(required=False)


class LinksInputUpdateSerializer(serializers.Serializer):
    name=serializers.CharField(required=False)
    link_reference=serializers.CharField(required=False)
    link_type=serializers.ChoiceField(
        choices=[l.name for l in LinkTypes],
        required=False
    )
    icon=serializers.CharField(required=False)

class LinksOutputSerializer(serializers.Serializer):
    id=serializers.UUIDField()
    name=serializers.CharField(allow_null=True)
    link_reference=serializers.CharField()
    link_type=serializers.CharField()
    icon=serializers.CharField(allow_null=True)

