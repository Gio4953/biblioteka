from django.shortcuts import render, redirect
from .forms import ReaderForm

def reader_create(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
    else:
        form = ReaderForm()
    return render(request, 'reader_create.html', {'form': form})
