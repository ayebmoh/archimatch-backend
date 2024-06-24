# Generated by Django 5.0.1 on 2024-04-28 15:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0045_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architectrequest',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Refused', 'Refused'), ('En attente Demo', 'En attente Demo'), ('En attente Decision', 'En attente Decision')], default='En attente Decision', max_length=255),
        ),
        migrations.CreateModel(
            name='Realization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categorie', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('surface', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('architect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='archimatch_app.architect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RealizationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/realizations/')),
                ('realisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='archimatch_app.realization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
