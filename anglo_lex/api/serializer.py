from rest_framework import serializers
from dictonary.models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
    # title = serializers.CharField(max_length=20)
    # description = serializers.CharField(allow_blank=True)
    # time_create = serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data):
    #     return Dictionary.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.create = validated_data.get("time_create", instance.time_create)
    #     instance.save()
    #     return instance
