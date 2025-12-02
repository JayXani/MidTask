from rest_framework import serializers
from ..Domain.entities import UserEntity
from enum import Enum

class Status(Enum):
    ACTIVATE = "A"
    BLOCKED = "B"
    DEACTIVATE = "D"


class UserInputSerializer(serializers.Serializer): 
    name = serializers.CharField()
    status = status = serializers.ChoiceField(
        choices=[s.name for s in Status],  # nomes da enum do domínio
    )
    email = serializers.CharField()
    password_hash = serializers.CharField()
    phone = serializers.CharField()
    login_type = serializers.CharField()
    ip_address = serializers.CharField()
    permissions = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False
    )
    created_at = serializers.DateField()
    updated_at = serializers.DateField()

    def to_internal_value(self, data): # Aqui que realizo a trativa dos dados para converter em objetos serializados
        validated = super().to_internal_value(data)
        validated["status"] = Status[validated["status"]]  # transforma string → enum
        return validated