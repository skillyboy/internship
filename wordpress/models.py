from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(max_length=50)
    answer1 = models.CharField(max_length=50)
    answer2 = models.CharField(max_length=50, blank=True, null=True)
    answer3 = models.CharField(max_length=50, blank=True, null=True)
    answer4 = models.CharField(max_length=50, blank=True, null=True)    
    def __str__(self):
        return self.question 

    class Meta:
        db_table = 'log'
        managed = True
        verbose_name = 'log'
        verbose_name_plural = 'logs'