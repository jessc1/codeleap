from rest_framework import serializers
from users.models import User

class UsersSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('username').read_only = True # setting username field to read_only
        
  

    class Meta:
        model = User
        fields = ['id', 'username','created',
                  'title', 'content']
