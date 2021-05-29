from django.shortcuts import render
import json
# Create your views here.
booksData = open(
    '/home/zer0x90/python/bookst/books.json').read()

data = json.loads(booksData)


def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)
 

def show(request, id):
    single_book = list()
    
    for book in data:
        if book['id'] == id:
            single_book = book

    context = {'book': single_book}
    return render(request, 'books/show.html', context)
 
