# Generated by Django 3.2.13 on 2022-09-18 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='final_comparison_data',
            old_name='MOH_Indicator_ID',
            new_name='MOH_FacilityID',
        ),
        migrations.RenameField(
            model_name='final_comparison_data',
            old_name='MOH_UID',
            new_name='MOH_IndicatorCode',
        ),
        migrations.RenameField(
            model_name='final_comparison_data',
            old_name='MOH_Indicator_Name',
            new_name='indicators',
        ),
    ]
