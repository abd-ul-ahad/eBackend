from django.urls import path
from .views import products_create_view, products_details_view


urlpatterns = [
    # http://127.0.0.1:8000/api/products/create/
    path('create/', products_create_view),
    # http://127.0.0.1:8000/api/products/2
    path('<int:pk>', products_details_view)
]
