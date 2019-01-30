from django.db import models

# Create your models here.
class equipment(models.Model):
        name = models.CharField(max_length=60,null=True)
        option = models.CharField(max_length=60,null=True)
        first = models.TextField(null=True)
        second = models.TextField(null=True)
        third = models.TextField(null=True)
