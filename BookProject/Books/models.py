from django.db import models


class Book(models.Model):
    Book_Title = models.CharField(max_length=100)
    Book_Author = models.CharField(max_length=100)
    Book_Genre = models.CharField(max_length=100)
    Book_Price = models.CharField(max_length=100)
    Book_Rating = models.CharField(max_length=100)
    Book_Date = models.CharField(max_length=100)

    def __str__(self):
        return self.Book_Title + ' - ' + self.Book_Author