# Generated by Django 5.0.1 on 2024-04-22 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0028_archisubscription_arch_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archisubscription',
            name='arch_id',
        ),
        migrations.AlterField(
            model_name='architect',
            name='subscription',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='archimatch_app.archisubscription'),
        ),
    ]
