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
    director = models.ForeignKey(Person, related_name='Director')
    actors = models.ManyToManyField(Person, through = 'Role')
    year = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.title, self. year)

class Role(models.Model):
    person =models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=64)

    def __str__(self):
        return "{} as {}".format(self.person, self.role)
