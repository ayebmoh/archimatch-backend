# Generated by Django 5.0.1 on 2024-04-24 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0043_goodtype_location_projectbudget_services_worksurface_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='arch_id',
        ),
    ]
