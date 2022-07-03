from django import forms

from book_app.models import Books, LargeCategory, SmallCategory


class LCSelect(forms.Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
    
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['largecategory-id'] = value.instance.large_category_id
        return option



class CategoryForm(forms.ModelForm):
    large_category = forms.ModelChoiceField(LargeCategory.objects)
    small_category = forms.ModelChoiceField(SmallCategory.objects, widget=LCSelect)

    class Meta:
        model = Books
        fields = ('title',)
    
    field_order = ('large_category', 'small_category', 'title')