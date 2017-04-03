from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKeyField(Person)
    actors = models.ManyToManyField(Person, related_name = 'role')
    year = models.IntegerField()
