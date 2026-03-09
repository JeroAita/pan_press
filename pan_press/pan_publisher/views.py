from django.shortcuts import render
# from django.http import HttpResponse
from .models import articles

# Index: una lista de los artículos que existen
def index(request):
    article_list = articles()
    return render(request, "pan_publisher/index.html", {"articles": article_list})

