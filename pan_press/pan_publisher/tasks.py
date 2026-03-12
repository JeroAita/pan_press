"""
Archivo con scripts a ejecutar periódicamente, configurados en apps.py.
"""
import os
from django.utils.text import slugify
from django.conf import settings
from .models import Article


# Escanear los artículos que existan en content/articles y
# mantiener actualizada la base de datos.
def scan_articles():
    CONTENT_DIR = os.path.join(settings.BASE_DIR.parent, "content", "articles")

    # Conjunto de carpetas existentes en disco.
    # os.listdir(path) devuelve todo archivo o subdirectorio contenido en path.
    # os.path.join(path, string) concatena la ruta con el nombre de archivo o subdirectorio,
    # os.path.isdir(path) devuelve verdadero si la ruta apunta a un directorio existente.
    dirs_on_disk = set()
    for d in os.listdir(CONTENT_DIR):
        d_full_path = os.path.join(CONTENT_DIR, d)
        if os.path.isdir(d_full_path):
            dirs_on_disk.add(d)

    # ^idem utilizando 'set comprehension' - sintaxis especial de Python.
    #dirs_on_disk = set(
    #    d for d in os.listdir(CONTENT_DIR)             #de la lista de directorios+archivos
    #    if os.path.isdir(os.path.join(CONTENT_DIR, d)) #tomar sólo los directorios.
    #)

    # Conjunto de carpetas existentes en la base de datos.
    # flat=True porque, por defecto, values_list devuelve tuplas (porque está pensado para
    # solicitar más de un dato de cada objeto de la clase).
    dirs_on_db = set(
        Article.objects.values_list("dir_path", flat=True)
    )

    # Crear registros para artículos nuevos
    # HARDCODED PLACEHOLDERS !!! Tomar de metadatos del markdown o generar.
    for dir_name in (dirs_on_disk - dirs_on_db):
        Article.objects.create(
            title = dir_name,
            author = "Unknown",
            wri_date = None,
            dir_path = dir_name
            title = "Unknown",
            author = "Unknown",
            wri_date = None,
            pub_date = "Today",
            slug_title = slugify(dir_name),
            dir_path = dir_name
        )

    # Borrar registros para artículos eliminados
    # Utilizando 'lookups' - sintaxis especial de Django: filter() con doble guión bajo.
    dirs_only_on_db = (dirs_on_db - dirs_on_disk)
    Article.objects.filter(dir_path__in=dirs_only_on_db).delete()
