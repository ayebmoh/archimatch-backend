# Generated by Django 5.0.1 on 2024-05-21 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0057_category_subcategory_alter_realization_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realization',
            name='categorie',
            field=models.ForeignKey(default='Category M', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Realizations', to='archimatch_app.category'),
        ),
    ]
