from django.contrib import admin
from .models import Book,Category,SubCategory
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['book_name','book_quantity','book_price','book_category']
admin.site.register(Book,BookAdmin)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name']
admin.site.register(SubCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
admin.site.register(Category,CategoryAdmin)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ['subcategory_name']
# admin.site.register(SubCategory)