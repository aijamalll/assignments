# Generated by Django 4.1.3 on 2022-12-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvparser',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
