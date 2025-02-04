# Generated by Django 5.0.1 on 2024-04-22 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0027_alter_architect_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='archisubscription',
            name='arch_id',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='architect',
            name='subscription',
            field=models.OneToOneField(default=2000, on_delete=django.db.models.deletion.CASCADE, to='archimatch_app.archisubscription'),
            preserve_default=False,
        ),
    ]
