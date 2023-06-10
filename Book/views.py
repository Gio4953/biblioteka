from django.shortcuts import render
from django.db.models import Prefetch
from .models import Book, Reader

def book_list(request):
    prefetch = Prefetch('readers', queryset=Reader.objects.only('name', 'surname', 'email'))
    books = Book.objects.prefetch_related(prefetch)
    book = Book.objects.create(title='დორიან გრეის პორტრეტი', author='ოსკარ უაილდი', publication_date='1890-01-01')
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
