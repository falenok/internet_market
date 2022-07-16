from django.db import models
from django.core.files import File
from django.utils.translation import gettext_lazy as _
from django.shortcuts               import render
from django.template                import RequestContext

# class CupManage(models.Manager):
#     def create_cup(self, type, color, surface, size, image):
#         book = self.create(title=title)
#         # do something with the book
#         return book





class Cup(models.Model):
    type = models.CharField(max_length=200, default='1')
    color = models.CharField(max_length=200, default='Белый')
    surface = models.CharField(max_length=200, default='Гладкая')
    size = models.CharField(max_length=200, default='Большой')
    image = models.ImageField(upload_to='images', default='1_aLvXjS4.png')

# class Cup_1(Cup):
#     type = "1"
#     color = "Белый1"
#     surface = "Гладкая1"
#     size = "Большой1"
#     image = "1_aLvXjS4.png"
Cup_1 = Cup("2","Тест","Тест","Бигтест",'1_aLvXjS4.png')
def Cup_out(Cup_1):
    return print(Cup_1.type,Cup_1.color,Cup_1.surface,Cup_1.size,Cup_1.image)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

