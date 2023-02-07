from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/productsapp/products/')
        else:
         print(form.errors.as_data()) # here you print errors to terminal    
    form = NewUserForm()    
    context={
        'form':form,
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')
    
def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user=user, image=image, contact_number=contact_number)
        profile.save()
    return render(request,'users/createprofile.html')
def seller_profile(request,id):
    seller = User.objects.get(id=id)
    context = {
        'seller' : seller,
    }
    return render(request,'users/sellerprofile.html',context)