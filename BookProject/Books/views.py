from django.http import Http404
from django.shortcuts import render
from .models import Book


def index(request):
    all_books = Book.objects.all()
    return render(request, 'BookList/index.html', {'all_books': all_books})


def detail(request, book_id):
    path = 'Books/index.html'
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        path = 'Books/404.html'
        raise Http404("Book does not exist")
    return render(request, path, {'book': book})


def home(request):
    return render(request, 'Home/index.html')
