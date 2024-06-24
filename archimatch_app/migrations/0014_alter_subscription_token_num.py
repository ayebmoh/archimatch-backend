# Generated by Django 5.0.1 on 2024-04-12 14:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0013_alter_subscription_token_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='token_num',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)]),
        ),
    ]
