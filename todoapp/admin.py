from django.contrib import admin
from .models import *
# Register your models here.

class AltKategoriSlug(admin.ModelAdmin):
    list_display = ["id","isim","slug"]

class KategoriAdmin(admin.ModelAdmin):
    list_display = ["id","isim","slug"]

admin.site.register(Kategori)
admin.site.register(AltKategoriler,AltKategoriSlug)
admin.site.register(ToDo)