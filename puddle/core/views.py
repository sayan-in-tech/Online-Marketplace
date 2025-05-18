from django.shortcuts import render

from item.models import Item, Category

def index(request):
    items = Item.objects.filter(is_sold=False)
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')