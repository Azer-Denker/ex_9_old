from django.contrib.auth import get_user_model
from rest_framework import serializers
from webapp.models import Photo


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True,
                                               view_name='api_v1:user-detail')

    class Meta:
        model = get_user_model()
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email']


class PhotoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True,
                                               view_name='api_v1:photo-detail')
    author_url = serializers.HyperlinkedRelatedField(read_only=True, source='author',
                                                     view_name='api_v1:user-detail')
    author = UserSerializer(read_only=True)

    class Meta:
        model = Photo
        fields = ['image', 'description', 'creation_date', 'author_name']
        read_only_fields = ('author',)
