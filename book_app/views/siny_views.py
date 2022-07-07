from django.shortcuts import render

from book_app.forms import *
from ..models import Books, LargeCategory, SmallCategory
from django.http.response import JsonResponse
from django.core import serializers
# Create your views here.


"""
SinyさんのAjax非同期通信の連動型プルダウンメニュー実装
https://sinyblog.com/django/django-dependent-chained-dropdown-selectlist/
"""

def getSmallcategories(request):
    print('①')
    large_category = request.POST.get('large_category')
    print('②')
    small_categories = serializers.serialize("json", return_small_categories_by_largeone(large_category))
    # small_categories = return_small_categories_by_largeone(large_category)
    print('③')
    print(small_categories)
    return JsonResponse({'small_categories': small_categories})
    # pk = []
    # small_categories_name = []
    # for c in small_categories:
    #     pk.append(c.pk)
    #     small_categories_name.append(c.name)

    # return JsonResponse({'name': small_categories_name})
    # return JsonResponse({'pk': pk, 'name': small_categories_name})

def send_form(request):
    context = {}
    if request.method == 'GET':
        form = LargeCategoryForm()
        context['form'] = form
        return render(request, 'add_books_siny.html', context)
    else:
        form = LargeCategoryForm(request.POST)
        if form.is_valid():
            selected_small_category = request.POST.get('small_category')
            selected_large_category = form(request.POST)
            print(selected_small_category)
            print(selected_large_category)
