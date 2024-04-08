# Generated by Django 4.1.7 on 2024-04-04 16:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notifications_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=100)),
                ('email_password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(8)])),
                ('email_host', models.CharField(default='mail.tdbsoft.co.ke', max_length=50)),
                ('email_port', models.CharField(default=465, max_length=5)),
                ('use_tls', models.BooleanField(default=True)),
                ('fail_silently', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Email Configuration',
            },
        ),
    ]