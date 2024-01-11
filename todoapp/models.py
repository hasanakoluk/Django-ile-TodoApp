from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Kategori(models.Model):
    isim = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = "isim")

    def __str__(self):
        return self.isim
    


class AltKategoriler(models.Model):
    isim = models.CharField(max_length = 50)
    slug = AutoSlugField(populate_from = "isim")

    def __str__(self):
        return self.isim
    



class ToDo(models.Model):
    baslik = models.CharField(max_length = 50)
    aciklama = models.TextField(max_length = 200)
    resim = models.FileField(upload_to="todo_resmi")
    kategori = models.ForeignKey(Kategori,on_delete= models.CASCADE)
    alt_kategoriler = models.ManyToManyField(AltKategoriler)
    slug = AutoSlugField(populate_from = "baslik")

    def __str__(self):
        return self.baslik
