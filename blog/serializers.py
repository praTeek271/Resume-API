from rest_framework import serializers
from .models import user_data


class UserDataSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'DOB', 'email', 'state', 'gender', 'resume', 'selected')
        model = user_data
