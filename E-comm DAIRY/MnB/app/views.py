
from django.shortcuts import render,redirect
from .models import Product,Customer
from django.views import View
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages

def home(request):
    return render(request,'app/index.html')

def aboutUs(request):
    return render(request,'app/about.html')

def contactUs(request):
    return render(request,'app/contact.html')


class categoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,'app/category.html',locals())

class categoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,'app/category.html',locals())


class productView(View):
    def get(self,request,pk):
         product=Product.objects.get(id=pk)
         return render(request,'app/productdetail.html',locals())
    

class customerRegistrationView(View):  
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request,'app/customerRegistration.html',locals())
    
    def post(self,request):
        form= CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulations user registered successfully")

        else:
            messages.error(request,"invalid data input")
        return render(request,'app/customerRegistration.html',locals())    
    
class ProfileView(View):
    def get(self,request):
            form= CustomerProfileForm()
            return render(request,'app/profile.html',locals()) 
    def post(self,request):
            form= CustomerProfileForm(request.POST)
            if form.is_valid():
                usr= request.user 
                name = form.cleaned_data['name']
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                zipcode = form.cleaned_data['zipcode']
                reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
                reg.save()
                messages.success(request, 'Congratulation!! Profile Updated Succesfully')
            else:
                messages.warning(request,"Invalid input data")
            return render(request,'app/profile.html',locals()) 

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form =CustomerProfileForm(instance=add)
        return render(request,'app/updateAddress.html',locals())
    
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'Congratulation!! Address Updated Succesfully')
        else:
            messages.warning(request,"Invalid input data")
        return redirect('address')

       