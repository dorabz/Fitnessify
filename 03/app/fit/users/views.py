from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect("login")

    else:
        form=UserRegisterForm()
        return render(request,"registration/register.html",{"form":form})


def home(request):
    if request.user.is_authenticated:
        return render(request,'users/home.html')
    else:
        return redirect('login')

@login_required
def myprofile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('myprofile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile/myprofile.html', context)



@login_required
def physical(request):
    if request.user.is_authenticated:
        return render(request,"profile/physical.html")
    else:
        return redirect('login')

@login_required
def diet(request):
    if request.user.is_authenticated:
        return render(request,"profile/diet.html")
    else:
        return redirect('login')

