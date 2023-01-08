# Generated by Django 4.1.3 on 2023-01-05 14:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labs', '0005_remove_lab_poc_manager_lab_poc_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='poc_manager',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
