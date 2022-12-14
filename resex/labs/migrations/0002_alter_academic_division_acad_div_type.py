# Generated by Django 4.1.3 on 2023-01-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic_division',
            name='acad_div_type',
            field=models.CharField(choices=[('Dept', 'Department'), ('Sch', 'School'), ('IDP', 'Interdisciplinary Program'), ('Cent', 'Centre')], default='Dept', max_length=4, verbose_name='Academic Division Type'),
        ),
    ]
