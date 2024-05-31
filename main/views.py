from urllib.request import Request
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .serializers import AreaSerializer, Construction_organizationSerializer, Construction_projectSerializer
from rest_framework import viewsets
from .models import Area, Construction_organization, Construction_project

class AreaViewSet(viewsets.ModelViewSet):
    """View for Area"""
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    class_permissions = (IsAuthenticated,)


class Construction_organizationViewSet(viewsets.ModelViewSet):
    """View for Construction_organization"""
    queryset = Construction_organization.objects.all()
    serializer_class = Construction_organizationSerializer
    class_permissions = (IsAuthenticated,)


class Construction_projectViewSet(viewsets.ModelViewSet):
    """View for Construction_project"""
    queryset = Construction_project.objects.all()
    serializer_class = Construction_projectSerializer
    class_permissions = (IsAuthenticated,)