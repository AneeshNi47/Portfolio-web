# Generated by Django 2.2.12 on 2020-05-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200)),
                ('contact_date', models.DateTimeField()),
                ('email', models.CharField(default='email', max_length=200)),
                ('subject', models.CharField(default='subject', max_length=200)),
                ('message', models.CharField(default='message', max_length=500)),
                ('status', models.CharField(default='Open', max_length=500)),
            ],
        ),
    ]
