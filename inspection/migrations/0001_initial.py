# Generated by Django 3.2.7 on 2021-10-07 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=10, null=True)),
                ('vehicle_category', models.CharField(choices=[('leka kola', 'leka kola'), ('bus', 'bus'), ('kamion', 'kamion')], max_length=100, null=True)),
                ('start_expl', models.CharField(max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_telnumber', models.CharField(max_length=10, null=True)),
                ('last_check', models.DateField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections', to='inspection.customer')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inspections', to='inspection.vehicle')),
            ],
        ),
    ]
