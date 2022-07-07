from django.urls import path
from . import views

app_name = 'book_app'

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('add_books/', views.add_books, name='add_books'),
    path('list_books_test/', views.list_books_test, name='list_books_test'),
    path('list_books_original/', views.list_books_original, name='list_books_original'),
    path('books/', views.books, name='books'),

    path('add_books_siny/', views.send_form, name='add_books_siny'),
    path('get_small_categories/', views.getSmallcategories, name='get_small_categories'),

    path('narito_jquery/', views.narito_jQuerybooks, name='narito_jquery'),
    path('narito_ajax/', views.narito_Ajaxbooks, name='narito_ajax'),
    path('ajax_get_category/', views.ajax_get_category, name='ajax_get_category'),

    path('outside_table/', views.outside_table, name='outside_table'),
]

htmx_urlpatterns = [
    path('sort/', views.sort, name='sort'),
]

urlpatterns += htmx_urlpatterns
