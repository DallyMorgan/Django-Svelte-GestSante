# Generated by Django 4.2.3 on 2024-02-27 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sante', '0003_remove_appareil_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='tel',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medecin',
            name='nom',
            field=models.CharField(max_length=255, verbose_name='Nom du medecin '),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sante.service')),
            ],
            options={
                'verbose_name_plural': 'Patients',
                'db_table': 'Patient',
            },
        ),
    ]
