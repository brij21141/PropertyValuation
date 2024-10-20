# Generated by Django 5.1 on 2024-09-16 13:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0002_companyprofile'),
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporterreport',
            name='datecreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporterreport',
            name='receptionid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reporterreport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reporterreport',
            name='userdetailsid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='propval.userdetails'),
        ),
    ]
