from django.contrib import admin
from .models import Book
from .models import Author


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', "price", 'market_price']
    list_display_links = []
    list_filter = ["id", 'title', "price", 'market_price']
    search_fields = ['title']
    list_editable = ['title']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', "email"]
    list_display_links = []
    list_filter = ['name', 'age', "email"]
    search_fields = ['name', 'email']
    list_editable = ['email']


# Register your models here.
admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
