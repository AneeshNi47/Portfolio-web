# Generated by Django 2.2.12 on 2020-05-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
                ('hashtags1', models.CharField(default='', max_length=200)),
                ('hashtags2', models.CharField(default='', max_length=200)),
                ('hashtags3', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stitle', models.CharField(default='null', max_length=200)),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
