from django.shortcuts import render

from book_app.forms import *
from ..models import Books, LargeCategory, SmallCategory
from django.http.response import JsonResponse
from django.core import serializers
# Create your views here.

def list_books(request):
    all_books = Books.objects.all().order_by('order')
    context = {
        'all_books': all_books,
    }
    return render(request, 'list_books.html', context)


def add_books(request):
    if request.method == 'GET':
        form = CategoryForm()
        context = {
            'form': form,
        }
        return render(request, 'add_books.html', context)
    else:
        large_category_id = request.POST.get('large_category')
        small_category_id = request.POST.get('small_category')
        title = request.POST.get('title')
        small_category = SmallCategory.objects.get(id=small_category_id)
        print('large_category:', end='')
        print(LargeCategory.objects.get(id=large_category_id))
        Books.objects.create(category=small_category, title=title)
        
        form = CategoryForm()
        context = {
            'form': form,
        }
        return render(request, 'add_books.html', context)

def list_books_test(request):
    all_books = Books.objects.all().order_by('order')
    context = {
        'all_books': all_books,
    }
    return render(request, 'list_books_test.html', context)

def list_books_original(request):
    all_books = Books.objects.all().order_by('order')
    context = {
        'all_books': all_books,
    }
    return render(request, 'list_books_original.html', context)

"""
YouTube BugBytes Sortable HTMX menuの実装
https://www.youtube.com/watch?v=V-f_yYKUJo8
https://www.youtube.com/watch?v=5Fuwo4tVXmE&t=952s
https://stackoverflow.com/questions/72863484/htmx-sortable-works-only-once-rendering-makes-it-disabled
https://htmx.org/examples/sortable/
"""


def books(request):
    all_books = Books.objects.all().order_by('order')
    context = {
        'all_books': all_books,
    }
    return render(request, 'books.html', context)

def sort(request):
    books_order_list = request.POST.getlist('book_order')
    print(books_order_list)
    all_books = []
    for idx, book_pk in enumerate(books_order_list, start=1):
        book = Books.objects.get(pk=book_pk)
        book.order = idx
        book.save()
        all_books.append(book)
    context = {
        'all_books': all_books,
    }
    return render(request, 'books.html', context)
    # return render(request, 'list_books.html', context)
    


"""
テーブルの外枠にボタンを配置したい試み
https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1418690729
"""
def outside_table(request):
    return render(request, 'outside_table.html')