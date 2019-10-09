from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """
    Name field serialization and it also takes care of
    validation rules internally.
    """
    name = serializers.CharField(max_length=50)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {"password": {
            "write_only": True,
            "style": {"input_type": "password"}
        }}

    def create(self, validated_data):
        """
        Create new User
        :param validated_data: Contains the user info
        :return: UserProfile object
        """
        user =  models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )
        return user
