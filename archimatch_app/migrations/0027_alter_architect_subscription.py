# Generated by Django 5.0.1 on 2024-04-22 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0026_alter_architect_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='subscription',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='archimatch_app.archisubscription'),
        ),
    ]
