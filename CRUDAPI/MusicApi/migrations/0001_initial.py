# Generated by Django 3.1.4 on 2021-01-10 13:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Genre', models.CharField(max_length=200)),
                ('Producer', models.ForeignKey(on_delete=models.SET('Unknown Producer'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
