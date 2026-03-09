from django.db import models

from pathlib import Path

# Directorio de contenido
CONTENT_DIR = Path(__file__).resolve().parent.parent.parent / "content/articles"

# La lista de artículos; uno por subdirectorio de CONTENT_DIR
def articles():
    return [d.name for d in CONTENT_DIR.iterdir() if d.is_dir()]
