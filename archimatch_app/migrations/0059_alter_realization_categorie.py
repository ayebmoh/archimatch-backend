# Generated by Django 5.0.1 on 2024-05-21 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0058_alter_realization_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realization',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Realizations', to='archimatch_app.category'),
        ),
    ]
