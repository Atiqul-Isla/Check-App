# Generated by Django 3.1.1 on 2022-06-26 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20220624_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
