from django.shortcuts import render
from django.conf import settings



def CreatorHome(request):
    return render(request, 'creator/creator_home.html')
