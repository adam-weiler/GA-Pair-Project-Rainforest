from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from rainforest.models import Product
from rainforest.forms import ProductForm

# import pdb

# NB: dont need to pass the request for a redirect


def root(request):
    return redirect(reverse("show_all"))


def show_all(request): #Renders a list of all products.
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "show_all.html", context)


def show_product(request, id): #Renders a single product.
    product = Product.objects.get(pk=id)
    context = {"product": product}
    return render(request, "show_product.html", context)


def new_product(request): #Renders a form to create a new product.
    form = ProductForm()
    context = {"form": form}
    return render(request, "product_form.html", context)


def create_product(request): #User creating a new product.
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("show_all"))
    else: #Else sends user back to new product form.
        context = {"form": form}
        return render(request, "product_form.html", context)


def edit_product(request, id): #Renders a form to edit an existing product.
    product = Product.objects.get(pk=id)
    form = ProductForm(instance=product)
    context = {"product": product, "form": form }
    return render(request, "edit_product_form.html", context)


def update_product(request, id): #User updating a new product
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect(reverse("show_all"))
    else: #Else sends user back to new product form.
        context = {"product": product, "form": form }
        return render(request, "edit_product_form.html", context)

