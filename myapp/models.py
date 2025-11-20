from django.db import models

class movie(models.Model):
    name =models.CharField(max_length=50)
    desc =models.TextField()
    img =models.ImageField()

    def __str__(self):
        return self.desc