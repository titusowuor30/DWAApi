# Generated by Django 3.2.13 on 2022-09-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20220927_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='final_comparison_data',
            name='category',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]