# Generated by Django 3.2.8 on 2021-10-12 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inspection', '0012_auto_20211012_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
