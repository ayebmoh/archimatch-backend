# Generated by Django 5.0.1 on 2024-04-22 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0025_archisubscription_remove_architect_sub_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='subscription',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='archimatch_app.archisubscription'),
        ),
    ]
