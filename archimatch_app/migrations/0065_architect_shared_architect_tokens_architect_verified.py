# Generated by Django 5.0.1 on 2024-05-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0064_alter_report_user_clientreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='architect',
            name='shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='architect',
            name='tokens',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='architect',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
