# Generated by Django 4.2.3 on 2024-02-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sante', '0004_medecin_tel_alter_medecin_nom_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='recu',
            field=models.BooleanField(default=False),
        ),
    ]
