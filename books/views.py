from django.shortcuts import render,redirect
from django.views.generic import View
from books.forms import BooksAppForm,BooksAppModelForm,RegistrationForm,LoginForm
from books.models import BooksApp
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator



def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

@method_decorator(signin_required,name="dispatch")
class BookAppCreateView(View):
    def get(self,request,*args,**kwagrs):
        form=BooksAppModelForm()
        return render(request,"book.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=BooksAppModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Added sucessfully")
            
            print("created")
            return render(request,"book.html",{"form":form})
        else:
    
            messages.error(request,"failed to add book")
            return render(request,"book.html",{"form":form})
        
@method_decorator(signin_required,name="dispatch")      
class BooksAppListView(View):
    def get(self,request,*args,**kwargs):
        qs=BooksApp.objects.all()
        authors=BooksApp.objects.all().values_list("author",flat=True).distinct()
        print(authors)
        if "author" in request.GET:
            auth=request.GET.get("author")
            qs=qs.filter(author__iexact=auth)
        return render(request,"book_list.html",{"data":qs,"authors":authors})
    
def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=BooksApp.objects.filter(name__icontains=name)
        return render(request,"book_list.html",{"data":qs})


@method_decorator(signin_required,name="dispatch")  
class BooksAppDetailVeiw(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=BooksApp.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})
    
@method_decorator(signin_required,name="dispatch")   
class BooksAppDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        BooksApp.objects.get(id=id).delete()
        messages.success(request,"employee has been deleted ")
        return redirect("books-all")
    
@method_decorator(signin_required,name="dispatch")    
class BooksAppUpdateView(View):
    def get(self,request,*args,**kwagrs):
        id=kwagrs.get("pk")
        obj=BooksApp.objects.get(id=id)
        form=BooksAppModelForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=BooksApp.objects.get(id=id)
        form=BooksAppModelForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"employee has been deleted ")

            return redirect("books-detail",pk=id)
        else:
           messages.error(request,"failed to update")
           return render(request,"book_edit.html",{"form":form})
        
        
class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # print("saved")
            messages.success(request," account has been created")

            return render(request,"register.html",{"form":form})
        else:
            # print("failed")
            messages.error(request,"failed")
            return render(request,"register.html",{"form":form})
        
class SignInView(View):
    def get(self,request,*args,**kwagrs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwagrs):
        form=LoginForm(request.POST)
     
        if form.is_valid():
            # print(request.user,"before")
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            # print(u_name,pwd)
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                print("valid credential")
                login(request,user_obj)
                # print(request.user,"after")
                return redirect("books-all")
            
        messages.error(request,"invalied credential")
        return render(request,"login.html",{"form":form})
    
@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
     def get(self,request,*args,**kwargs):
         logout(request)
         return redirect("signin")



