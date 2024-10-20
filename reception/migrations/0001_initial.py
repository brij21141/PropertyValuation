# Generated by Django 5.1 on 2024-08-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptionReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicationdate', models.DateTimeField()),
                ('applicationnumber', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('bankname', models.CharField(max_length=50)),
                ('bankvertical', models.CharField(max_length=50)),
                ('add1', models.CharField(max_length=100)),
                ('add2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=10)),
                ('visitingperson', models.CharField(max_length=30)),
                ('reportperson', models.CharField(max_length=30)),
            ],
        ),
    ]
