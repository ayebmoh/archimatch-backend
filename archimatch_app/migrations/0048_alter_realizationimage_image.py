# Generated by Django 5.0.1 on 2024-04-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0047_rename_realisation_realizationimage_realization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizationimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/realizations/'),
        ),
    ]
