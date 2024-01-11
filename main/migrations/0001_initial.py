# Generated by Django 5.0 on 2024-01-06 21:04

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategoriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='isim')),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='isim')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50)),
                ('aciklama', models.TextField(max_length=200)),
                ('resim', models.FileField(upload_to='todo_resmi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik')),
                ('alt_kategoriler', models.ManyToManyField(to='main.altkategoriler')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kategori')),
            ],
        ),
    ]
