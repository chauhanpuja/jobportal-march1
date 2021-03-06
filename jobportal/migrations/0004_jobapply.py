# Generated by Django 3.2.5 on 2022-01-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0003_rename_address_job_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('criteria', models.CharField(max_length=200)),
                ('exp', models.IntegerField()),
            ],
        ),
    ]
