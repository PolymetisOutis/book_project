from django.urls import path
from . import views

app_name = 'book_app'

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('add_books/', views.add_books, name='add_books'),
    path('list_books_test/', views.list_books_test, name='list_books_test'),
    path('list_books_original/', views.list_books_original, name='list_books_original'),
    path('books/', views.books, name='books'),
]

htmx_urlpatterns = [
    path('sort/', views.sort, name='sort'),
]

urlpatterns += htmx_urlpatterns
