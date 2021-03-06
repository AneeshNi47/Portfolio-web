# Generated by Django 2.2.12 on 2020-05-12 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_jobimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(default='', max_length=200)),
                ('service_icon', models.ImageField(upload_to='image/')),
                ('service_description', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_point', models.CharField(default='', max_length=200)),
                ('service_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Services')),
            ],
        ),
    ]
