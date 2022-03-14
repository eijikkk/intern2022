# Generated by Django 4.0 on 2022-03-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microhr', '0004_alter_application_pass_or_fail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='pass_or_fail',
        ),
        migrations.AddField(
            model_name='application',
            name='is_passed',
            field=models.BooleanField(null=True, verbose_name='合否'),
        ),
    ]