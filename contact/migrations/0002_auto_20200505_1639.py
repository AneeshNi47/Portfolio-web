# Generated by Django 2.2.12 on 2020-05-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(default='message', max_length=2000),
        ),
    ]
