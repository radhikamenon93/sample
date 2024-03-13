from django.db import models

class Employee(models.Model):
    email=models.EmailField(null=True)
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)

class Emp(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=20)

class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    year=models.PositiveIntegerField()
    genre=models.CharField(max_length=20)

class Bookm(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=30)
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.name

   






