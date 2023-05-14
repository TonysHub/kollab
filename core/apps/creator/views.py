from django.shortcuts import render


def CreatorHome(request):
    return render(request, "creator/creator_home.html")
