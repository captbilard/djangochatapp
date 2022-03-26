from django.db import models

# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Rooms"
    
    def __str__(self):
        return self.name