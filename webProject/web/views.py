from django.shortcuts import render
from .models import Ethnos, Article

# Create your views here.
def index(request):
    return render(request, "index.html")
def ethnoses(request):
    data = Ethnos.objects.all()
    return render(request, "ethnoses.html", {"eth": data})
def ethnos(request, id):
    data = Article.objects.filter(ethnos__id=id)
    return render(request, "ethnos.html", {"data": data})
def article(request, ethnosId, articleId):
    data = Article.objects.get(id=articleId)
    return render(request, "article.html", {"data": data})