from django.shortcuts import render, get_object_or_404
# from .models import Order

from .models import Articles , Order
# Create your views here.
def search_home(request):
    search = Articles.objects.all()
    return render(request, 'main/product.html', {'search': search})

# views.py

# def track_order(request):
#     order = None
#     if request.method == 'POST':
#         form = OrderSearchForm(request.POST)
#         if form.is_valid():
#             order_number = form.cleaned_data['order_number']
#             order = get_object_or_404(Order, order_number=order_number)
#     else:
#         form = OrderSearchForm()
#
#     return render(request, 'track_order.html', {'form': form, 'order': order})

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Order
from .forms import OrderSearchForm

def track_order(request):
    order = None
    if request.method == 'POST':
        form = OrderSearchForm(request.POST)
        if form.is_valid():
            order_number = form.cleaned_data['order_number']
            order = get_object_or_404(Order, order_number=order_number)
    else:
        form = OrderSearchForm()

    return render(request, 'search/track_order.html', {'form': form, 'order': order})


from django.shortcuts import render
from .models import Order

def search(request):
    order_number = request.GET.get('order_number')
    order = None
    if order_number:
        try:
            order = Order.objects.get(order_number=order_number)
        except Order.DoesNotExist:
            order = None
    return render(request, 'search.html', {'order': order})
