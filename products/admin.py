from django.contrib import admin

from .models import Product, Category

class SubCategoryInline(admin.TabularInline):  # or admin.StackedInline
    model = SubCategory
    extra = 1
    
#@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('name')
    #search_fields = ('name')
    inlines = [SubCategoryInline]
    

"""@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('subcategory',)
    """
admin.site.register(Product)