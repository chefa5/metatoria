from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    image = models.ImageField(upload_to='users', blank=True, null=True, verbose_name='Avatar')
    about_me = models.TextField(blank=True, null=True, verbose_name='About Me')
    tg_contact = models.URLField(max_length=50, blank=True, null=True, verbose_name='TG')
    vk_contact = models.URLField(max_length=50, blank=True, null=True, verbose_name='VK')
    phone_number = PhoneNumberField(region="RU", blank=True, null=True, verbose_name='Phone')
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.username