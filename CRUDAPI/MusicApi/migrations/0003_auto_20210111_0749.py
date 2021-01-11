# Generated by Django 3.1.4 on 2021-01-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicApi', '0002_auto_20210110_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='Rental',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('No information'), to='MusicApi.rentals'),
        ),
        migrations.AlterField(
            model_name='rentals',
            name='rental',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
