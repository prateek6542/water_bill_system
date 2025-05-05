from django.urls import path
from .views import bill_view

urlpatterns = [
    path('', bill_view, name='bill'),
]
