"""rainforest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rainforest import views

urlpatterns = [
    path("", views.root),
    path("admin/", admin.site.urls),
    path("products", views.show_all, name="show_all"),
    path("products/<int:id>", views.show_product, name="show_product"),
    path("products/new", views.new_product, name="new_product"),
    path("products/create", views.create_product, name="create_product"),
]
