# Generated by Django 5.0.1 on 2024-04-12 07:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0007_architect_categories_architect_complexity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Sub_type', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=800)),
                ('Start_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('End_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('Token_num', models.IntegerField(verbose_name=range(5, 50))),
                ('Price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
