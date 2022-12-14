# Generated by Django 4.1.3 on 2022-12-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cinema_delete_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_note', models.CharField(max_length=100)),
                ('description_note', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('quantity_note', models.IntegerField()),
                ('trailer_note', models.URLField()),
                ('genre_note', models.CharField(choices=[('HORROR', 'HORROR'), ('ANIME', 'ANIME'), ('COMEDY', 'COMEDY'), ('FANTASY', 'FANTASY'), ('ROMANTIC', 'ROMANTIC'), ('DRAMMA', 'DRAMMA')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Model_notes_of_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_note', models.CharField(max_length=200)),
                ('text_note', models.TextField()),
                ('date_note', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
