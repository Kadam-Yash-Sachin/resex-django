# Generated by Django 4.1.3 on 2023-01-05 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labs', '0006_alter_lab_poc_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='poc_manager',
        ),
        migrations.AddField(
            model_name='lab',
            name='poc_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
