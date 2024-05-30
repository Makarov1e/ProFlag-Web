from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def search(request):
    return render(request, 'main/search.html')

def user(request):
    return render(request, 'main/user.html')


