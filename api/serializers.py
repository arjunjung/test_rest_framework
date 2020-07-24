from rest_framework import serializers
from api.models import ToyModel

class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    was_included_in_home = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return ToyModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.category = validated_data.get('category',instance.category)
        instance.category = validated_data.get('category',instance.category)
        instance.was_included_in_home = validated_data.get('was_included_in_home',instance.was_included_in_home)
        instance.save()
        return instance
