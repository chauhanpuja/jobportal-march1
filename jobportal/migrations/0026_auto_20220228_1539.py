# Generated by Django 3.2.5 on 2022-02-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0025_addjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjob',
            name='company_name',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addjob',
            name='logo',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
