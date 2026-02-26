from rest_framework import serializers
from ..Domain.enum.StatusEnum import Status


class UserInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    status = serializers.ChoiceField(
        choices=[s.name for s in Status],  # nomes da enum do domínio
    )
    email = serializers.EmailField(
        required=True
    )
    password = serializers.CharField(required=True)
    avatar=serializers.CharField(required=False)
    phone = serializers.CharField()
    ip_address = serializers.IPAddressField()
    created_at = serializers.DateField(required=False)
    updated_at = serializers.DateField(required=False)

    def to_internal_value(self, data): # Aqui que realizo a trativa dos dados para converter em objetos serializados
        validated = super().to_internal_value(data)
        validated["status"] = Status[validated["status"]]  # transforma string → enum
        return validated


class GoogleOauthSerializer(serializers.Serializer):
    use_email = serializers.EmailField(required=True)
    google_id=serializers.CharField(required=True)
    ip_address=serializers.CharField(required=True)

# Recomendado ter serializers diferente para cada tipo de método, para nao gerar bugs
class UserUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    status = serializers.ChoiceField(
        choices=[s.name for s in Status],
        required=False
    )
    avatar=serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    def validate(self, data):
        if "password" in data and len(data["password"]) < 8:
            raise serializers.ValidationError({
                "password": ["Password must be at least 8 characters"]
            })
        return data

    def to_internal_value(self, data):
        validated = super().to_internal_value(data)
        if "status" in validated:
            validated["status"] = Status[validated["status"]]
        return validated


class UserOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    status = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(allow_null=True)
    avatar=serializers.CharField()
    login_type = serializers.CharField()
    ip_address = serializers.IPAddressField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    

