# Generated by Django 3.0.3 on 2021-09-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0002_search_result_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_result',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
