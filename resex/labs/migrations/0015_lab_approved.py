# Generated by Django 4.1.3 on 2023-02-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0014_remove_lab_associated_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
