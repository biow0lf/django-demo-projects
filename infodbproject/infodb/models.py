from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    bio = models.TextField()
    contacts = models.TextField()
    dob = models.DateField()

    class Meta:
        verbose_name_plural = "People"
