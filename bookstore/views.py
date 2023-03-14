from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bookstore.models import Book

# Create your views here.


def all_books(request):
    books = Book.objects.filter(is_active=True).order_by("market_price")
    return render(request, 'bookstore/showAll.html', locals())


def edit_price(request):
    book_id = request.GET['id']
    title = request.GET['title']
    pub = request.GET['pub']
    price = request.GET['price']
    mkt_price = request.GET['mkt_price']
    return render(request, 'bookstore/edit_price.html', locals())


def do_edit(request):
    book_id = request.POST['book_id']
    price = request.POST['price']
    mkt_price = request.POST['mkt_price']
    book = Book.objects.get(id=book_id)
    book.price = price
    book.market_price = mkt_price
    book.save()
    return HttpResponseRedirect("/bookstore/bookshelf/")


def do_delete(request):
    book = Book.objects.get(id=request.GET['book_id'])
    book.is_active = False
    book.save()
    return HttpResponseRedirect("/bookstore/bookshelf/")
