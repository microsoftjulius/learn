from django.db import models


# Create your models here.
class Pages(models.Model):
    uuid = models.UUIDField()
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.text[:50]
