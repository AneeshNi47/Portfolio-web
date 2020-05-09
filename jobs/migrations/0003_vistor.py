# Generated by Django 2.2.12 on 2020-05-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200426_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vistor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userip', models.GenericIPAddressField()),
                ('visit_date', models.DateTimeField()),
            ],
        ),
    ]