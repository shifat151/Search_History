# Generated by Django 3.0.3 on 2021-09-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_result',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]