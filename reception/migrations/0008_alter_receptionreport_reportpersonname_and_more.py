# Generated by Django 5.1 on 2024-09-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0007_receptionreport_reportpersonname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receptionreport',
            name='reportpersonname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='receptionreport',
            name='visitingpersonname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
