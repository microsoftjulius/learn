from django.db import models
from django.urls import reverse


# Create your models here.
class Pages(models.Model):
    uuid = models.UUIDField()
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):  # new
        return reverse('post_detail', args=[str(self.id)])
