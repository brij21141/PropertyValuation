# Generated by Django 5.1 on 2024-10-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0017_document_reporterholdcause'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='reporterholdcause',
        ),
        migrations.AddField(
            model_name='receptionreport',
            name='reporterholdcause',
            field=models.TextField(blank=True, null=True),
        ),
    ]
