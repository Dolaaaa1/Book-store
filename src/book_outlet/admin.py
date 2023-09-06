from django.contrib import admin
from .models import Book , Auther , Address , Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    #readonly_fields =("slug",)
    prepopulated_fields ={"slug":("title",)}
    list_filter = ("auther","rating",)
    list_display = ("title","auther",)

admin.site.register(Book  ,BookAdmin)
admin.site.register(Auther)
admin.site.register(Address)
admin.site.register(Country)
