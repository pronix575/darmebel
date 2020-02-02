from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    preview = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=50)
    preview = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name        

class Work(models.Model):
    name = models.CharField(max_length=50)
    preview = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(default="")

    views = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Request(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)

    created_date = models.DateTimeField(default=timezone.now)
    
    is_viewed = models.BooleanField(default="False")
    is_alive = models.BooleanField(default="True")

class MainPagePreview(models.Model):
    name = models.CharField(max_length=50)
    preview = models.ImageField(upload_to='images/')
    description = models.TextField(default="")

    def __str__(self):
        return self.name