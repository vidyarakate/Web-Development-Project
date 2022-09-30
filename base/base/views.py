from atexit import register
from multiprocessing import context
from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from mob.models import Customer
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from mob.forms import CreateUserForm
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()

        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user )

                return redirect('login')

        context={
            'form':form,
        }
        return render(request,'register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')

            else:
                messages.info(request,'Username OR password is incorrect')
                
        context={}
        return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def INDEX(request):
    emp=Customer.objects.all()

    context={
        'emp':emp,
    }
    return render(request,'index.html',context)

def ADD(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        plan=request.POST.get('plan')
        status=request.POST.get('status')

        emp=Customer(
            name=name,
            address=address,
            phone=phone,
            city=city,
            pincode=pincode,
            plan=plan,
            status=status,
        )

        emp.save()
        return redirect('home')

    return render(request,'index.html')


def Edit(request):
    emp=Customer.objects.all()

    context={
        'emp':emp,
    }
    return render(request,'index.html',context)



   
def Update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        plan=request.POST.get('plan')
        status=request.POST.get('status')

        emp=Customer(
            id=id,
            name=name,
            address=address,
            phone=phone,
            city=city,
            pincode=pincode,
            plan=plan,
           
            status=status,
        )
        emp.save()
        return redirect('home')
    return redirect(request,'index.html')

def Delete(request,id):
    emp=Customer.objects.filter(id=id)
    emp.delete()
    context={
        'emp':emp,
    }
    return redirect('home')
