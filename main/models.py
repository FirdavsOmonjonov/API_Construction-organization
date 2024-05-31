from django.db import models


class Area(models.Model):
    """Model for Area"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Construction_organization(models.Model):
    """Model for Construction organizations"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    founded = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Construction_project(models.Model):
    """Model for Construction Projects"""
    Construction_organization = models.ForeignKey(Construction_organization, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    floors= models.IntegerField()
    parking = models.BooleanField(default=False)
    playground = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)

    def __str__(self):
        return self.name