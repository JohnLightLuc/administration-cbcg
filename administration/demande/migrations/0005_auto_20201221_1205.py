# Generated by Django 3.1.4 on 2020-12-21 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demande', '0004_auto_20201221_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attestationconge',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='congeprof', to='demande.professeur'),
        ),
        migrations.AlterField(
            model_name='certificatpriseservice',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priseserviceprof', to='demande.professeur'),
        ),
        migrations.AlterField(
            model_name='certificattravail',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travailprof', to='demande.professeur'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professeur', to=settings.AUTH_USER_MODEL),
        ),
    ]