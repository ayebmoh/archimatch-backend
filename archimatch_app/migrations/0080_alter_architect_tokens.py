# Generated by Django 4.2 on 2024-06-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0079_supplier_chosen_spec_alter_archimatchuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='tokens',
            field=models.IntegerField(default=5),
        ),
    ]
