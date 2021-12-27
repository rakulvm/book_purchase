from django.db import models

# Create your models here.
class register_user(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=1000)

class book_details(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField()
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name+" - "+self.author
