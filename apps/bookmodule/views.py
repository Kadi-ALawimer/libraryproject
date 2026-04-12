from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def index(request): 
    return HttpResponse("Hello, world!") 

def index(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)


# Task 4 + 5 
def home(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})



# Task 6 

def index2(request, val1):
    return HttpResponse(f"value1 = {val1}")



# Task 6 (index2 Error) 

def index2_text(request):
    return HttpResponse("error, expected val1 to be integer")



# Task 7 

def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    return render(request, 'bookmodule/show.html', {'book': targetBook})
from django.shortcuts import render

def index(request):
    return render(request, 'bookmodule/index.html')

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')

def html5_formatting(request):
    return render(request, 'bookmodule/html5_formatting.html')

def html5_lists(request):
    return render(request, 'bookmodule/html5_lists.html')

def html5_tables(request):
    return render(request, 'bookmodule/html5_tables.html')

    from django.shortcuts import render
#lab 6 task 1


#lab 6 task 2
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble'}
    book2 = {'id':56788765,'title':'Reversing', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'Machine Learning', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
        .filter(title__icontains='and')\
        .filter(edition__gte=2)\
        .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')