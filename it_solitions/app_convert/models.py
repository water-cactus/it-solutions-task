from django.db import models


# Create your models here.
class Input_users(models.Model):
    text = models.CharField('Введенный текст', max_length=250)

    def __str__(self):
        return self.text

