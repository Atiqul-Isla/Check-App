# Generated by Django 4.0.5 on 2022-06-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='chatRoom',
        ),
    ]
