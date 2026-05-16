from django.urls import path 
from . import views




urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path ("html5/links", views.links),
    path("search",views.search),
    #path('add/books', views.add_books, name='add_books'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'),
    path('part1/listbooks',views.listbooks_part1,name='listbooks_part1'),
    path('lab11/task1/list', views.list_s1, name='list_s1'),
path('lab11/task1/add', views.add_s1, name='add_s1'),
path('lab11/task1/update/<int:id>', views.update_s1, name='update_s1'),
path('lab11/task1/delete/<int:id>', views.delete_s1, name='delete_s1'),

path('lab11/task2/list', views.list_s2, name='list_s2'),
path('lab11/task2/add', views.add_s2, name='add_s2'),

path('lab11/task3/list', views.list_i1, name='list_i1'),
path('lab11/task3/add', views.add_i1, name='add_i1'),

    
        ]
