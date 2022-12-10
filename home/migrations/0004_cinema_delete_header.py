# Generated by Django 4.1.3 on 2022-12-01 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_header_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
                ('trailer', models.URLField()),
                ('genre', models.CharField(choices=[('HORROR', 'HORROR'), ('ANIME', 'ANIME'), ('COMEDY', 'COMEDY'), ('FANTASY', 'FANTASY'), ('ROMANTIC', 'ROMANTIC'), ('DRAMMA', 'DRAMMA')], max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Header',
        ),
    ]