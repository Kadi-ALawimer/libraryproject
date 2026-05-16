from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import Book
from django.db.models import Q, Count, Sum,Avg,Max,Min


# def index(request): task1 lab 3
#     return HttpResponse("hello, world") 


# def index(request): #task 2 lab 3
#     name = request.GET.get("name") or "world!"
#     return HttpResponse("Hello "+name) 

# def index2(request, number=0):
#     return HttpResponse("value = " + str(number))


# def index (request):
#     name = request.GET.get("name") or "world"
#     return render(request , "bookmodule/index.html",{"name":name})




def index2(request, number=0):
    return HttpResponse("value = " + str(number))


def viewbook(request, bookId):

    book1 = {
        'id': 123,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley'
    }

    book2 = {
        'id': 456,
        'title': 'Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1

    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}

    return render(request, 'bookmodule/show.html', context)



def index (request):
    return render(request , "bookmodule/index.html")

def list_books (request):
    return render(request , "bookmodule/list_books.html")

def viewbook (request):
    return render(request , "bookmodule/one_book.html")

def aboutus (request):
    return render(request , "bookmodule/aboutus.html")



def __getBookList():
    book1= {
        'id':12344321,
        'title':'continous Delivery',
        'author':'J.Humble and D.far'
    }

    book2 = {
        'id' :'56788765',
        'title':'Reversing',
        'author':'E.Eliam'

    }

    return[book1,book2]

#LAB5
def links(request):
    return render(request, "bookmodule/links.html")

#lab6
def search(request):

    if request.method == "POST":

        string = request.POST.get('keyword').lower()

        isTitle = request.POST.get('option1')

        isAuthor = request.POST.get('option2')

        books = __getBookList()

        newBooks = []

        for item in books:

            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(
            request,
            'bookmodule/list_books.html',
            {'books': newBooks}
        )

    return render(request, "bookmodule/search.html")



def simple_query(request):
    mybooks = Book.objects.filter(title__icontains = 'and')
    return render(request , "bookmodule/list_books.html", {'books':mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains = 'and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks)>=1:
        return render(request , "bookmodule/list_books.html", {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def lab8_task1(request):
    books= Book.objects.filter(Q(price__lte=80))
    return render(request,'bookmodule/list_books.html',{'books':books})


def lab8_task2(request):
    books = Book.objects.filter(Q(edition__gt=3)& (Q(title__icontains='qu')| Q(author__icontains='qu')))
    return render(request,'bookmodule/list_books.html',{'books':books})                             

def lab8_task3(request):
    books = Book.objects.filter(~Q(edition__gt=3) &~ (Q(title__icontains='qu')| Q(author__icontains='qu')))
    return render(request,'bookmodule/list_books.html',{'books':books})   

def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request,'bookmodule/list_books.html',{'books':books})   

def lab8_task5(request):
    result = Book.objects.aggregate(
        total_books = Count('id'),
        total_price = Sum('price',default = 0),
        average_price = Avg('price', default =0),
        max_price=Max('price'),
        min_price= Min('price')

    )
    return render(request,'bookmodule/stats.html',{'result':result})   



from .models import Student, Address
from django.db.models import Count
from django.shortcuts import render
from django.db.models import Count, Sum, Avg, Max, Min, Q
from .models import Book, Publisher, Author

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/city_students.html', {'cities': cities})

from django.shortcuts import render
from django.db.models import Sum, Min, Avg, Max, Count, Q
from .models import Book, Publisher


def lab9_task1(request):
    books = Book.objects.all()
    total_books = 350

    for book in books:
        book.percentage = (book.quantity / total_books) * 100

    return render(request, 'bookmodule/lab9_books.html', {'books': books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(
        total_stock=Sum('book__quantity')
    )
    return render(request, 'bookmodule/lab9_publishers.html', {'publishers': publishers})


def lab9_task3(request):
    publishers = Publisher.objects.annotate(
        oldest_book=Min('book__pubdate')
    )
    return render(request, 'bookmodule/lab9_publishers.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        average_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_publishers.html', {'publishers': publishers})


def lab9_task5(request):
    high_rated = Count('book', filter=Q(book__rating__gte=7))

    publishers = Publisher.objects.annotate(
        highly_rated_books=high_rated,
        total_quantity=Sum('book__quantity')
    )

    return render(request, 'bookmodule/lab9_publishers.html', {'publishers': publishers})


def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        book_count=Count(
            'book',
            filter=Q(book__price__gt=50) &
                   Q(book__quantity__lt=5) &
                   Q(book__quantity__gte=1)
        )
    )

    return render(request, 'bookmodule/lab9_publishers.html', {'publishers': publishers})



def listbooks_part1(request):
    books=Book.objects.all()
    return render(request , 'part1/bookmodule/listbooks.html',{'books':books})


def addbook_part1(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author =request.POST.get('author')
        price= request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(
            title=title,author=author,price=float(price),edition=int('edition')

        )
        return redirect('listbooks')
    return render(request,'part1/bookmodule/listbooks.html')



def listbooks_part2(request):
    books = Book.objects.all()
    return render (request, 'bookmodule/part2/listbooks.html',{'books':books})


# def addbook_part2(request):
#     if request.method =='POST':
#         form = Bookform(request.POST)
#         if form.is_valid():
#             return redirect ('listbooks_part2')
#     else:
#         form= Bookform()

#     return render (request, 'bookmodule/part2/listbooks.html',{'form':form})    


# def editbook_part2(request, id):
#     book = Book.objects.get(id=id)

#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)

#         if form.is_valid():
#             form.save()
#             return redirect('listbooks_part2')
#     else:
#         form = BookForm(instance=book)

    return render(request, 'bookmodule/part2/formbook.html', {'form': form})

def deletebook_part2(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('listbooks_part2')


from django.shortcuts import render, redirect

from .models import (
    S1,
    S2,
    I1
)

from .forms import (
    S1Form,
    S2Form,
    I1Form
)


# =========================
# TASK 1
# =========================

def list_s1(request):

    objs = S1.objects.all()

    return render(
        request,
        'bookmodule/list_s1.html',
        {'objs': objs}
    )


def add_s1(request):

    if request.method == 'POST':

        form = S1Form(request.POST)

        if form.is_valid():

            form.save()

            return redirect('list_s1')

    else:

        form = S1Form()

    return render(
        request,
        'bookmodule/s1_form.html',
        {'form': form}
    )


def update_s1(request, id):

    obj = S1.objects.get(id=id)

    if request.method == 'POST':

        form = S1Form(
            request.POST,
            instance=obj
        )

        if form.is_valid():

            form.save()

            return redirect('list_s1')

    else:

        form = S1Form(instance=obj)

    return render(
        request,
        'bookmodule/s1_form.html',
        {'form': form}
    )


def delete_s1(request, id):

    obj = S1.objects.get(id=id)

    if request.method == 'POST':

        obj.delete()

        return redirect('list_s1')

    return render(
        request,
        'bookmodule/delete_s1.html',
        {'obj': obj}
    )


# =========================
# TASK 2
# =========================

def list_s2(request):

    objs = S2.objects.all()

    return render(
        request,
        'bookmodule/list_s2.html',
        {'objs': objs}
    )


def add_s2(request):

    if request.method == 'POST':

        form = S2Form(request.POST)

        if form.is_valid():

            form.save()

            return redirect('list_s2')

    else:

        form = S2Form()

    return render(
        request,
        'bookmodule/s2_form.html',{'form': form}
    )


# =========================
# TASK 3
# =========================

def list_i1(request):

    objs = I1.objects.all()

    return render(
        request,
        'bookmodule/list_i1.html',
        {'objs': objs}
    )

@login_required(login_url='login')
def add_i1(request):

    if request.method == 'POST':

        form = I1Form(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('list_i1')

    else:

        form = I1Form()

    return render(
        request,
        'bookmodule/i1_form.html',
        {'form': form}
    )