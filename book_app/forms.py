from django import forms

from book_app.models import Books, LargeCategory, SmallCategory

"""
https://github.com/Gilfeather さんの連動型プルダウンメニューのプラン
"""
class LCSelect(forms.Select):
    def __init__(self, attrs=None, choices=()):
        super(LCSelect, self).__init__(attrs, choices)
    
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['largecategory-id'] = value.instance.large_category_id
            print('value:', end='')
            print(value)
            print('value.instance')
            print(value.instance)
        return option



class CategoryForm(forms.ModelForm):
    large_category = forms.ModelChoiceField(LargeCategory.objects, empty_label='---大カテゴリーを選択---')
    small_category = forms.ModelChoiceField(SmallCategory.objects, widget=LCSelect, empty_label='選択してください')

    class Meta:
        model = Books
        fields = ('title',)
    
    field_order = ('large_category', 'small_category', 'title')

"""
SinyさんのAjax非同期通信での連動型プルダウンメニュー実装
"""

def get_large_categories():
    all_large_categories = [('------', '---大カテゴリーを選択---')]
    large_categories = LargeCategory.objects.all()
    for large_category in large_categories:
        all_large_categories.append((large_category.name, large_category.name))
    return all_large_categories

def return_small_categories_by_largeone(large_category):
    all_small_categories = SmallCategory.objects.filter(large_category__name=large_category)
    return all_small_categories

class LargeCategoryForm(forms.Form):
    large_categories = forms.ChoiceField(
        choices = get_large_categories(),
        required = False,
        label = '大カテゴリー',
        widget = forms.Select(attrs={'id': 'id_large_categories'})
    )

"""
Narito先生の連動型プルダウンメニューについてのプラン
"""
class NaritoForm(forms.ModelForm):
    large_category = forms.ModelChoiceField(
        label='大カテゴリー',
        queryset=LargeCategory.objects,
        required=False,
        empty_label='---大カテゴリーを選択---'
    )
    
    class Meta:
        model = Books
        fields = ('category', 'title')
    
    field_order = ('large_category', 'category', 'title')