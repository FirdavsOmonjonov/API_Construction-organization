from django.contrib import admin
from .models import  Area, Construction_organization, Construction_project


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_link = ('id', 'name')


@admin.register(Construction_organization)
class ConstructionorganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'founded','area'  )
    list_display_link = ('id', 'name')


@admin.register(Construction_project)
class ConstructionprojectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','Construction_organization', 'area','field','floors','parking', 'playground', 'lift'  )
    list_display_link = ('id', 'name')