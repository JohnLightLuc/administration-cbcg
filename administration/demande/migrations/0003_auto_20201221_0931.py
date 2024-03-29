# Generated by Django 3.1.4 on 2020-12-21 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0002_auto_20201220_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificatpriseservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('matricule', models.CharField(max_length=255)),
                ('emploi', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('etat', models.CharField(default='En attente', max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('prof', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='priseserviceprof', to='demande.professeur')),
            ],
            options={
                'verbose_name': 'certificat de prise de service',
                'verbose_name_plural': 'certificats de prise de service',
            },
        ),
        migrations.DeleteModel(
            name='Certificatprisetravail',
        ),
    ]
