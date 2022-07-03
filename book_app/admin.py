from django.contrib import admin

from book_app.models import Books, LargeCategory, SmallCategory

# Register your models here.


admin.site.register(LargeCategory)
admin.site.register(SmallCategory)
admin.site.register(Books)