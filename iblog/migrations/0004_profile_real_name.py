# Generated by Django 3.0.9 on 2020-08-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iblog', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='real_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]