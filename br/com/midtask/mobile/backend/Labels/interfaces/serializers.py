from rest_framework import serializers

class LabelInputSerializer(serializers.Serializer):
    labels=serializers.ListField(
        child=serializers.CharField(max_length=30),
        required=True
    )

    def validate(self, attrs):
        dict_attrs = dict(attrs)
        if(not len(dict_attrs.get('labels'))): raise Exception('You can sended the labels')
        return attrs
    

class LabelOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()