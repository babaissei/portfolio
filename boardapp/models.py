from django.db import models
from django.utils import timezone

# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='',null=True,blank=True)
    good = models.IntegerField(null=True,blank=True, default=0)
    read = models.IntegerField(null=True,blank=True, default=0)
    readtext = models.CharField(max_length=200,null=True,blank=True, default='s')
    maketime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
