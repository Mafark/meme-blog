from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    class Meta():
        db_table = 'categoryy'
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Meme(models.Model):
    class Meta():
        db_table = 'Memasiki'
    image = models.ImageField(
        "Картинка мема", upload_to='images/')
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    category = models.ForeignKey(Category)
