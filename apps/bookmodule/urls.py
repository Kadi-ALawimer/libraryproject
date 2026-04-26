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
    path('books/lab8/task1', views.task1),
    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7),
    path('lab9/task1', views.lab9_task1),#lab 9
    path('lab9/task2', views.lab9_task2),#lab 9
    path('lab9/task3', views.lab9_task3),#lab 9
    path('lab9/task4', views.lab9_task4),#lab 9
    path('lab9/task5', views.lab9_task5),#lab 9
    path('lab9/task6', views.lab9_task6),#lab 9
]

