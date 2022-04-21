from pyexpat import model
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Ethnos(models.Model):
    name = models.CharField(max_length=255)
    brief_text = models.TextField("")
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    head = models.CharField(max_length=255)
    body = models.TextField("")
    image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now=True)
    ethnos = models.ForeignKey(Ethnos, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.head

class Contribution(models.Model):
    head = models.CharField(max_length=255)
    body = models.TextField("")
    date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.head