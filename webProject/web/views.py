from django.shortcuts import render, redirect
from .models import Ethnos, Article
from .forms import articleEdit

# Create your views here.
def index(request):
    return render(request, "index.html")
def ethnoses(request):
    data = Ethnos.objects.all()
    return render(request, "ethnoses.html", {"eth": data})
def ethnos(request, id):
    data = Article.objects.filter(ethnos__id=id)
    ethnos = Ethnos.objects.get(id=id)
    return render(request, "ethnos.html", {"data": data, "ethnos": ethnos})
def article(request, ethnosId, articleId):
    data = Article.objects.get(id=articleId)
    return render(request, "article.html", {"data": data})
def article(request, ethnosId, articleId):
    data = Article.objects.get(id=articleId)
    return render(request, "article.html", {"data": data})
def edit(request, ethnosId, articleId):
    data = Article.objects.get(id=articleId)
    if request.method == 'POST':
        data.head = request.POST.get("head")
        data.body = request.POST.get("body")
        data.save()
        return redirect('/ethnos/' + str(data.ethnos.id) + '/article/' + str(data.id))
    else:
        form = articleEdit(initial={'head': data.head, 'body': data.body})
        return render(request, "edit.html", {"form": form, "data": data})