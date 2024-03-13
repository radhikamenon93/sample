from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm,BookForm,BookmForm,StudentForm
from work.models import Emp,Book,Bookm,Student

class Empl(View):
    def get(self,request):
     form=EmpForm()
     return render(request,"add.html",{"form":form})
    def post(self,request):
       form=EmpForm(request.POST)
       if form.is_valid():
          print(form.cleaned_data)
          Emp.objects.create(**form.cleaned_data)
          return render(request,"add.html",{"form":form})
       else:
          return render(request,"add.html",{"form":form})
          

# Create your views here.
class Bookview(View):
    def get(self,request):
     form=BookForm()
     return render(request,"book.html",{"form":form})
    def post(self,request):
       form=BookForm(request.POST)
       if form.is_valid():
          print(form.cleaned_data)
          Book.objects.create(**form.cleaned_data)
          return render(request,"book.html",{"form":form})
       else:
          return render(request,"book.html",{"form":form})
       
class Bookmview(View):
    def get(self,request):
     form=BookmForm()
     return render(request,"bookm.html",{"form":form}) 

    def post(self,request):
      form=BookmForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request,"bookm.html",{"form":form}) 
      else:
          return render(request,"bookm.html",{"form":form}) 
      
class Booklist(View):
   def get(self,request):
      qs=Bookm.objects.all()  
      return render(request,"booklist.html",{"qs":qs})   
   def post(self,request):
      title=request.POST.get("p")
      qs=Bookm.objects.filter(title=title)
      return render(request,"booklist.html",{"qs":qs})


      
   
class Bookone(View):
   def get(self,request,*args,**kwargs):
      print(kwargs)
      id=kwargs.get("pk")
      qs=Bookm.objects.get(id=id)
      return render(request,"bookon.html",{"data":qs})
   
class bookdel(View):
   def get(self,request,*args,**kwargs):
      
      id=kwargs.get("pk")
      Bookm.objects.get(id=id).delete()
      return redirect('book-al')

class Bookupdate(View):   
   def get(self,request,*args,**kwargs):
      
      k=kwargs.get("pk")
      obj=Bookm.objects.get(id=k)
      form=BookmForm(instance=obj)
      return render(request,"bookedit.html",{"form":form})
   def post(self,request,*args,**kwargs):
      k=kwargs.get("pk")
      obj=Bookm.objects.get(id=k)
      form=BookmForm(request.POST,instance=obj)
      if form.is_valid():
         form.save()
      else:
         print("getout")
      return redirect('book-al')   
   
 





class Studentmview(View):
   def get(self,request):
     form=StudentForm()
     return render(request,"studm.html",{"form":form}) 
   def post(self,request):
      form=StudentForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request,"studm.html",{"form":form}) 
      else:
          return render(request,"studm.html",{"form":form}) 
      
class Studentlist(View):
   def get(self,request):
      qs=Student.objects.all()  
      return render(request,"studlist.html",{"qs":qs})  

class Studentone(View):
   def get(self,request,*args,**kwargs):
      print(kwargs)
      id=kwargs.get("ab")
      qs=Student.objects.get(id=id)
      return render(request,"studon.html",{"data":qs})   

class Studdel(View):
   def get(self,request,*args,**kwargs):
      
      id=kwargs.get("ab")
      Student.objects.get(id=id).delete()
      return redirect('stud-a')   
        




    

