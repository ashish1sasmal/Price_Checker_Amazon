# Generated by Django 3.0.2 on 2020-02-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_profile_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
