from django.urls import path
from .views import Get_Products, Post_Products

urlpatterns = [
    path('', Get_Products),
    path('post', Post_Products)
]
