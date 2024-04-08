from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title[0:25]
