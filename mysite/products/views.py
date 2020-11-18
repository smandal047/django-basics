from django.shortcuts import render
from .models import Product
from .form import ProductForm


# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    form_status = False
    if form.is_valid():
        form.save()
        form = ProductForm()
        form_status = True

    context = {
        'form': form,
        'form_status': form_status
    }
    return render(request, 'products/create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context = {
        'id': obj.id,
        'title': obj.title,
        'description': obj.description,
        'price': obj.price,
        'summary': obj.summary,
        'featured': obj.featured,
    }
    return render(request, 'products/detail.html', context)
