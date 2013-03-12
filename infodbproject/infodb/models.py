from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    contacts = models.TextField()

    class Meta:
        verbose_name_plural = "People"
