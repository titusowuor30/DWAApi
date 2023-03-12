# Generated by Django 4.1.7 on 2023-03-12 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleScreens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screens', models.TextField(max_length=2500)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
            options={
                'verbose_name_plural': 'Role Screens',
                'db_table': 'role_screens',
            },
        ),
    ]