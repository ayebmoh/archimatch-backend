# Generated by Django 5.0.1 on 2024-04-12 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0011_rename_end_date_subscription_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='option2',
            new_name='archi_supp',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='option3',
            new_name='proj_exposition',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='option1',
            new_name='prop_platform',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='option4',
            new_name='prop_profil',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='option5',
            new_name='prop_project',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='option6',
            new_name='realization_expo',
        ),
    ]
