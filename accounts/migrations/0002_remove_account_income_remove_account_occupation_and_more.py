# Generated by Django 5.0.6 on 2024-06-16 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='income',
        ),
        migrations.RemoveField(
            model_name='account',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='account',
            name='risk_appetite',
        ),
    ]
