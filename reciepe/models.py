from django.db import models

# Create your models here.
class Recipe(models.Model):
    reciepe_name = models.TextField(max_length=100)
    procedure = models.TextField()
    img = models.ImageField(upload_to="receipe")
    

    def __str__(self):
        return self.reciepe_name


