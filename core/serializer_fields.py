import uuid

from rest_framework import serializers


class UUIDRelatedField(serializers.Field):
    def __init__(self, model, *args, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        assert isinstance(value, uuid.UUID)
        return str(value)

    def to_internal_value(self, data):
        instance = self.get_instance(data)
        return instance.id

    def get_instance(self, data):
        try:
            instance = self.model.objects.get(id=self.build_uuid(data))
            return instance
        except self.model.DoesNotExist:
            raise serializers.ValidationError(f'{self.model.__name__} dosent exist')

    @staticmethod
    def build_uuid(data):
        try:
            return uuid.UUID(data)
        except ValueError:
            raise serializers.ValidationError('UUID Invalid')
