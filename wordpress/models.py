from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog = models.TextField(max_length=50)
    
    def __str__(self):
        return self.title 

    class Meta:
        db_table = 'log'
        managed = True
        verbose_name = 'log'
        verbose_name_plural = 'logs'