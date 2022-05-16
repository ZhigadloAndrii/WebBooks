from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_field = ['name']
    save_on_top = True


@admin.register(Language)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_field = ['name']
    save_on_top = True


@admin.register(Version)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_field = ['name']
    save_on_top = True


@admin.register(Author)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_for_link']
    list_display_links = ['id', 'name', 'name_for_link']
    search_field = ['name', 'name_for_link']
    save_on_top = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id',  'name', 'name_for_link', 'fk_section_id']
    list_display_links = ['id',  'name', 'name_for_link']
    search_field = ['name', 'name_for_link']
    save_on_top = True


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_for_link']
    list_display_links = ['id', 'name', 'name_for_link']
    search_field = ['name']


class VersionForBooksInline(admin.TabularInline):
    model = VersionsBooks
    extra = 0


class LanguageForBooksInline(admin.TabularInline):
    model = LanguagesBooks
    extra = 0


class PhotoForBooksInline(admin.TabularInline):
    model = PhotoForBooks
    extra = 0


class CharacteristicsBooksInline(admin.TabularInline):
    model = CharacteristicsBooks
    extra = 0


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'sale_price', 'in_stock', 'is_enable', 'count', 'fk_author_id',
                    'fk_category_id']
    list_display_links = ['id', 'title']
    search_field = ['id', 'title']
    inlines = [
        VersionForBooksInline,
        LanguageForBooksInline,
        PhotoForBooksInline,
        CharacteristicsBooksInline,
    ]
    save_on_top = True