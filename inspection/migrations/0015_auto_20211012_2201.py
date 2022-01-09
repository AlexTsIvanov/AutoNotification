# Generated by Django 3.2.8 on 2021-10-12 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inspection', '0014_alter_inspection_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inspections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections', to='inspection.vehicle'),
        ),
    ]
