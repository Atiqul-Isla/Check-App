# Generated by Django 3.1.1 on 2022-06-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20220624_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['-date_updated', '-date_created', '-Completed']},
        ),
        migrations.AlterField(
            model_name='list',
            name='Completed',
            field=models.BooleanField(default=False),
        ),
    ]
