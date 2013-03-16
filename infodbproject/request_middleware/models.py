from django.db import models


class RequestModel(models.Model):
    secure = models.BooleanField()
    path = models.TextField()
    get = models.TextField()
    post = models.TextField()
    cookies = models.TextField()
