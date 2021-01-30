# Generated by Django 3.1.4 on 2020-12-21 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demande', '0003_auto_20201221_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeur',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professeur', to=settings.AUTH_USER_MODEL),
        ),
    ]
