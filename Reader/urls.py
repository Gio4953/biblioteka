from django.urls import path
from Reader import views

urlpatterns = [
    path('create/', views.reader_create, name='reader_create'),
]
