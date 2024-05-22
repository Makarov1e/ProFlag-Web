from django.shortcuts import render
from .models import Articles
# Create your views here.
def search_home(request):
    search = Articles.objects.all()
    return render(request, 'main/product.html', {'search': search})



