from django.db import models

# Create your models here.
class Card(models.Model):
    number = models.PositiveIntegerField(unique=True, default=1)  # Нумерация с единицы
    name = models.CharField(max_length=255, blank=True, null=True)  # Имя карточки
    description = models.TextField(blank=True, null=True)  # Описание карточки
    photo = models.ImageField(upload_to='images', blank=True, null=True)  # Фотография карточки
    def __str__(self):
        return f'{self.number}. {self.name}'
    class Meta:
        db_table = 'Card'
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'