from django.urls import path
from Book import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
]
