# Generated by Django 3.2.7 on 2021-10-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0005_auto_20211009_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='client_telnumber',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='reg_number',
            field=models.SlugField(max_length=8, null=True),
        ),
    ]
