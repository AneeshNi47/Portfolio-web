# Generated by Django 2.2.12 on 2020-05-13 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='user_email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='QuoteRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=200)),
                ('user_email', models.CharField(default='', max_length=200)),
                ('project_desc', models.CharField(default='', max_length=2000)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=6)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(default='Requested', max_length=200)),
                ('project_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Services')),
            ],
        ),
    ]
