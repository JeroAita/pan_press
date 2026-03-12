from django.db import models

from pathlib import Path

# Modelo para artículos. Los artículos son creados/destruídos de la DB
# según existan en el directorio 'content/articles/' periódicamente por
# el programa en tasks.py.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    wri_date = models.DateTimeField("date written")
    pub_date = models.DateTimeField("date published")
    slug_title = models.SlugField(max_length=150, unique=True) # titulo sin caracteres especiales ni espacios, para ser URI válido.
    dir_path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pub_date:%Y-%m-%d}-{self.title}"

