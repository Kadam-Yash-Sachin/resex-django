# Generated by Django 4.1.3 on 2023-01-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0008_alter_lab_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_division',
            name='email',
            field=models.EmailField(blank=True, max_length=128, verbose_name='Email Address'),
        ),
    ]
