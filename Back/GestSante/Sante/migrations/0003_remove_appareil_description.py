# Generated by Django 5.0.2 on 2024-02-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sante', '0002_remove_service_appareils_appareil_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appareil',
            name='description',
        ),
    ]
