from django.urls import path, include

from djangosocialmedia.blog.apis.products import ProductApi

urlpatterns = [
    path('products/', ProductApi.as_view(), name='product')
]
