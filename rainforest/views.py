from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from rainforest.models import Product
from rainforest.forms import ProductForm

# import pdb

# NB: dont need to pass the request for a redirect


def root(request):
    return redirect(reverse('show_all'))


def show_all(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'show_all.html', context)


def show_product(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    return render(request, 'show_product.html', context)


def new_product(request):
    form = ProductForm()
    context = {'form': form}
    return render(request, 'product_form.html', context)
