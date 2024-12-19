from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='New')
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Date')

    def __str__(self):
        return f'{self.date}. {self.name}'
    
    class Meta:
        db_table = 'New'
        verbose_name = 'New'
        verbose_name_plural = 'News'