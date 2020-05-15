# Generated by Django 2.2.12 on 2020-05-12 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_servicepoints_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('comment', models.CharField(default='', max_length=500)),
                ('user_name', models.CharField(default='', max_length=200)),
                ('verification', models.CharField(default='Unverified', max_length=200)),
                ('project_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Services')),
            ],
        ),
    ]