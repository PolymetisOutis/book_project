from django.http.response import JsonResponse
from django.shortcuts import render
from book_app.forms import *
from ..models import Books, LargeCategory, SmallCategory

def narito_jQuerybooks(request):
    form = NaritoForm()
    large_category_list = LargeCategory.objects.all()
    context = {
        'form': form,
        'large_category_list': large_category_list,
    }
    return render(request, 'narito_jquery.html', context)

def narito_Ajaxbooks(request):
    form = NaritoForm()
    context = {
        'form': form
    }
    return render(request, 'narito_ajax.html', context)

def ajax_get_category(request):
    pk = request.POST.get('pk')
    # pkパラメータがない、もしくはpk=空文字列だった場合は全カテゴリを返しておく。
    if not pk:
        # category_list = SmallCategory.objects.all()
        category_list = []

    # pkがあれば、そのpkでカテゴリを絞り込む
    else:
        category_list = SmallCategory.objects.filter(large_category__pk=pk)

    # [ {'name': 'サッカー', 'pk': '3'}, {...}, {...} ] という感じのリストになる。
    category_list = [{'pk': category.pk, 'name': category.name} for category in category_list]

    # JSONで返す。
    return JsonResponse({'categoryList': category_list})