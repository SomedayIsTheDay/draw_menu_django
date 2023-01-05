from django.shortcuts import render


def index(request):
    return render(request, "mainapp/index.html", context={"title": "index"})


def any_url(request, item):
    return render(request, "mainapp/index.html", context={"title": item})


def any_url2(request, item, link):
    return render(request, "mainapp/index.html", context={"title": link})


def any_url3(request, item, link, sublink):
    return render(request, "mainapp/index.html", context={"title": sublink})
