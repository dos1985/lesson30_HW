
from rest_framework import serializers, status
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from users.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

    # def to_representation(self, instance):
    #     return instance.name


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True)
    # locations = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     queryset=Location.objects.all(),
    #     slug_field="name"
    # )

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "role", "age", "location"]


class UserCreateUpdateSerializer(ModelSerializer):
    location = SlugRelatedField(slug_field="name", many=True, queryset=Location.objects.all(), required=False)

    def is_valid(self, *, raise_exception=False):
        for loc_name in self.initial_data.get("location", []):
            loc, _ = Location.objects.get_or_create(name=loc_name)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = "__all__"

class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"





