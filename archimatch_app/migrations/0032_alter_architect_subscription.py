# Generated by Django 5.0.1 on 2024-04-22 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0031_alter_architect_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='subscription',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='archimatch_app.archisubscription'),
        ),
    ]
