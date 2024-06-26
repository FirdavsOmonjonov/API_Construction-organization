# Generated by Django 5.0.6 on 2024-05-31 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Construction_organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('founded', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.area')),
            ],
        ),
        migrations.CreateModel(
            name='Construction_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('floors', models.IntegerField()),
                ('parking', models.BooleanField(default=False)),
                ('playground', models.BooleanField(default=False)),
                ('lift', models.BooleanField(default=False)),
                ('Construction_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.construction_organization')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.area')),
            ],
        ),
    ]
