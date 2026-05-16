from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)


    from django.db import models


# =========================
# TASK 1
# =========================

class A1(models.Model):

    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class S1(models.Model):

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    address = models.ForeignKey(
        A1,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# =========================
# TASK 2
# =========================

class A2(models.Model):

    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class S2(models.Model):

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    addresses = models.ManyToManyField(A2)

    def __str__(self):
        return self.name


# =========================
# TASK 3
# =========================

class I1(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='images/'
    )

    def __str__(self):
        return self.name