from rest_framework import serializers
from enum import Enum

class Status(Enum):
    ACTIVATE = "A"
    BLOCKED = "B"
    DEACTIVATE = "D"


class UserInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    status = serializers.ChoiceField(
        choices=[s.name for s in Status],  # nomes da enum do domínio
    )
    email = serializers.EmailField(
        required=True
    )
    password_hash = serializers.CharField(required=False)
    phone = serializers.CharField()
    login_type = serializers.CharField()
    ip_address = serializers.IPAddressField()
    permissions = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=True
    )
    created_at = serializers.DateField(required=False)
    updated_at = serializers.DateField(required=False)

    def validate(self, data):
        dict_data = dict(data)
        login_type = dict_data.get("login_type")
        if(login_type != "google" and not dict_data.get("password_hash")):
            raise serializers.ValidationError({
                "password_hash": ["Password is required !"]
            })
        
        return data

    def to_internal_value(self, data): # Aqui que realizo a trativa dos dados para converter em objetos serializados
        validated = super().to_internal_value(data)
        validated["status"] = Status[validated["status"]]  # transforma string → enum
        return validated
    