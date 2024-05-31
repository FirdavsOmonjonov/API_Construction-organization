from rest_framework import serializers
from .models import Area, Construction_organization, Construction_project

class AreaSerializer(serializers.ModelSerializer):
    """Serializer for Area"""
    class Meta:
        model = Area
        fields = '__all__'


class Construction_organizationSerializer(serializers.ModelSerializer):
    """Serializer for Construction_organization"""
    class Meta:
        model = Construction_organization
        fields = '__all__'


class Construction_projectSerializer(serializers.ModelSerializer):
    """Serializer for Construction_project"""
    class Meta:
        model = Construction_project
        fields = '__all__'

