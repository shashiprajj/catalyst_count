# Generated by Django 5.0.6 on 2024-07-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst_builder_app', '0003_alter_companydata_city_alter_companydata_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='industry',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='size_range',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
