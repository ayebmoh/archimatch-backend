# Generated by Django 5.0.1 on 2024-05-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0061_report_archireport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='client',
        ),
        migrations.AlterField(
            model_name='archireport',
            name='status',
            field=models.CharField(default='Non-traité', max_length=255),
        ),
    ]
