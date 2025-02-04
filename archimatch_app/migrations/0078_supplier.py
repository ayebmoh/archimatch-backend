# Generated by Django 4.2 on 2024-05-30 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('archimatch_app', '0077_invitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('supplier_avatar', models.ImageField(blank=True, null=True, upload_to='SupplierAvatars/')),
                ('adress', models.CharField(default='', max_length=255, null=True)),
                ('bio', models.TextField(default='', max_length=1000, null=True)),
                ('company_name', models.CharField(default='', max_length=255, null=True)),
                ('registration_number', models.CharField(default='', max_length=255, null=True)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='CompanyLogos/')),
                ('first_cnx', models.BooleanField(default=False)),
                ('video_presentation', models.FileField(blank=True, null=True, upload_to='ArchitectVideos/')),
                ('categories', models.CharField(blank=True, default='need1', max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Architects',
            },
        ),
    ]
