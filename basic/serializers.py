from rest_framework import serializers
from .models import Registro

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('id', 'name', 'email', 'message', 'color', 'fruit', 'created_at')
        read_only_fields = ('id', 'created_at')