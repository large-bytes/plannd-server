from django.shortcuts import render
from .models import Article
from django.http import JsonResponse

# from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def article_list(request):
    # articles = Article.objects.all()
    # return JsonResponse(articles, safe=False)

    results = {"id": {"value": "1"}, "name": {"first": "Mega", "last": "Tron"}}
    return JsonResponse(results)
    # need to  figure out how to send data from querysets to the client

    # return render(request, "articles/article_list.html", {"articles": articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {"article": article})


# @login_required(login_url="/accounts/login/")
def article_create(request):
    form = forms.CreateArticle()
    return render(request, "articles/article_create.html"), {"form": form}
