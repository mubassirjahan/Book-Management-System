from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('mystery', 'Mystery'),
        ('fantasy', 'Fantasy'),
        ('biography', 'Biography'),
        ('science', 'Science'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)

    def __str__(self):
        return self.title