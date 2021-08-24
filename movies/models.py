from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(blank=True)
    persons = models.ManyToManyField('Person',
                                     related_name='movies',
                                     through='MovieCrew')
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    genders = ((MALE, 'Male'), (FEMALE, 'Female'))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=genders)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Role(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
