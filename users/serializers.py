from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField()
  

    class Meta:
        model = User
        fields = ['id', 'username','created',
                  'title', 'content']
