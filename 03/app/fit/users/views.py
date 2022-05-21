from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.urls import reverse_lazy

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, RecipeForm, IngredientFormSet

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


class ExerciseCreateView(CreateView):
    model = Exercise
    fields = ["exercise_name", "calories_burned", "sets", "reps", "weight"]
    success_url = reverse_lazy("exercise_list") #problem

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ExerciseListView(ListView):
    model = Exercise
    context_object_name = "exercises" # friendly queryset name for the template
    paginate_by = 10 

    def get_queryset(self):
        result = super(ExerciseListView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Exercise.objects.filter(exercise_name__contains=query,created_by=self.request.user )
            result = postresult
        else:
            result = Exercise.objects.filter(created_by=self.request.user)
        return result
        #user = self.request.user
        #return Exercise.objects.filter(created_by=user)

class ExerciseDetailView(DetailView):
    model = Exercise
    context_object_name = "exercise"


class ExerciseUpdateView(UpdateView):
    model = Exercise
    fields = ["exercise_name", "calories_burned", "sets", "reps", "weight"]

    def get_success_url(self):
        return reverse_lazy("exercise_detail", kwargs={'pk': self.object.pk})

    def test_func(self):
        exercise = self.get_object()
        return self.request.user == exercise.created_by

class ExerciseDeleteView(DeleteView):
    model = Exercise
    success_url = reverse_lazy("exercise_list")

    def test_func(self):
        exercise = self.get_object()
        return self.request.user == exercise.created_by

class RecipeListView(ListView):
    model = Recipe
    context_object_name = "recipes" # friendly queryset name for the template
    paginate_by = 10 

    def get_queryset(self):
        result = super(RecipeListView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Recipe.objects.filter(recipe_name__contains=query,created_by=self.request.user )
            result = postresult
        else:
            result = Recipe.objects.filter(created_by=self.request.user)
        return result

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'users/recipe_form.html'
    form_class = RecipeForm
    success_url = reverse_lazy("recipe_list")

    def get_context_data(self, **kwargs):
        data = super(RecipeCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST)
        else:
            data['ingredients'] = IngredientFormSet()
        return data
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)