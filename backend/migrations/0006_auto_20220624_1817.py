# Generated by Django 3.1.1 on 2022-06-24 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20220624_0028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['-date_updated', '-date_created']},
        ),
    ]
