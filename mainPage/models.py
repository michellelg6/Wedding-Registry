from django.db import models

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length = 100)
    caption = models.TextField(max_length = 500)
    image = models.ImageField(upload_to='mainPage/images')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
        
    
class Item(models.Model):
    title = models.CharField(max_length = 100)
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    caption = models.TextField(max_length = 500)
    image = models.ImageField(upload_to='mainPage/images')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title