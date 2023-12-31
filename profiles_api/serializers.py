from rest_framework import serializers
from profiles_api.models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API View"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User Profile Object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password',
                },
            }
        }

    def create(self, validated_data):
        """Create and return a new User"""
        user = UserProfile.objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password'),
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes a User Profile Feed Item Object"""

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'status_text', 'user', 'created_at', 'updated_at')
        extra_kwargs = {
            'user': {
                'read_only': True,
            }
        }
