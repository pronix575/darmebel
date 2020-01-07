from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    preview = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=50)
    preview = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class PreviewWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)