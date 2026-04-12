from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),                 # Template (Task 4/5)
    path('hello/', views.index),          # Task 1/2 (HttpResponse)
    path('index2/text/', views.index2_text),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),
        path('', views.index, name='books.index'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
    path('aboutus/', views.aboutus, name='books.aboutus'),
    path('html5/links/', views.html5_links, name="books.html5.links"),
    path('html5/formatting/', views.html5_formatting, name='books.html5.formatting'),
    path('html5/lists/', views.html5_lists, name='books.html5.lists'),
    path('html5/tables/', views.html5_tables, name='books.html5.tables'),
    path('search/', views.search, name='books.search'), #lab 6 task 1
   path('simple/query', views.simple_query),
path('complex/query', views.complex_query),
]

