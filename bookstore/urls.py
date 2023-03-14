from django.urls import path

from bookstore import views

urlpatterns = [
    path('bookshelf/', views.all_books),
    path('bookshelf/editPrice/', views.edit_price),
    path('bookshelf/editPrice/doEdit/', views.do_edit),
    path('bookshelf/doDelete/', views.do_delete)
]

