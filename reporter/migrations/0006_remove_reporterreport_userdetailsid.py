# Generated by Django 5.1 on 2024-09-19 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0005_alter_reporterreport_userdetailsid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporterreport',
            name='userdetailsid',
        ),
    ]
