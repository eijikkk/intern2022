# Generated by Django 4.0 on 2022-03-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microhr', '0002_application'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(fields=('user', 'work'), name='application_unique'),
        ),
    ]