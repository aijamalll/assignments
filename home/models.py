from django.db import models

class Cinema(models.Model):
    GENRE = (
        ('HORROR', "HORROR"),
        ("ANIME", "ANIME"),
        ("COMEDY", "COMEDY"),
        ("FANTASY", "FANTASY"),
        ("ROMANTIC", "ROMANTIC"),
        ("DRAMMA", "DRAMMA")
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField()
    trailer = models.URLField()
    genre = models.CharField(choices=GENRE, max_length=100)

    def __str__(self):
        return self.title

class Cinema_notes(models.Model):
    GENRE = (
        ('HORROR', "HORROR"),
        ("ANIME", "ANIME"),
        ("COMEDY", "COMEDY"),
        ("FANTASY", "FANTASY"),
        ("ROMANTIC", "ROMANTIC"),
        ("DRAMMA", "DRAMMA")
    )

    title_note = models.CharField(max_length=100)
    description_note = models.TextField()
    image = models.ImageField()
    quantity_note = models.IntegerField()
    trailer_note = models.URLField()
    genre_note = models.CharField(choices=GENRE, max_length=100)

    def __str__(self):
        return self.title_note

class Model_notes_of_user(models.Model):
    title_note = models.CharField(max_length=200)
    text_note = models.TextField()
    date_note = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title_note