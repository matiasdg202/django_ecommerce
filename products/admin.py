from django.contrib import admin

from .models import Product, Category, Section


class CategoryInline(admin.TabularInline):  # or admin.StackedInline
    model = Category
    extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

    inlines = [CategoryInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    search_fields = ("name",)
    list_filter = ("category",)
