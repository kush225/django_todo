from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TodoModel
from .forms import TodoForm, UserRegisterForm, UserUpdateForm

def index(request):
    context = { "title" : "index" }
    return render(request, 'todo/index.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('mainpage')
    else:
        form = UserRegisterForm()
    context = {"form" : form,
               "title": "Sign Up"}
    return render(request, 'registration/register.html', context)

@login_required
def mainpage(request):
    todo_list = TodoModel.objects.filter(author=request.user).order_by('date_posted')
    form = TodoForm()
    context = {
        "todo_list": todo_list,
        "form": form,
        "title": "main"
    }
    return render(request, 'todo/mainpage.html', context)

@login_required
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = TodoModel(title=form.cleaned_data['title'], author=request.user)
        new_todo.save()

    return redirect('mainpage')

@login_required
def completeTodo(request, todo_id):
    todo = TodoModel.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('mainpage')

@login_required
def deleteCompleted(request):
    TodoModel.objects.filter(author_id=request.user.id).filter(completed__exact=True).delete()

    return redirect('mainpage')

@login_required
def deleteAll(request):
    TodoModel.objects.filter(author_id=request.user.id).all().delete()

    return redirect('mainpage')

@login_required
def deleteSelected(request):
    todo_id_list = request.GET.getlist('checks')
    TodoModel.objects.filter(author_id=request.user.id).filter(id__in=todo_id_list).delete()
    return redirect('mainpage')

@login_required()
def logout_view(request):
    logout(request)
    return redirect("index")

@login_required()
def settings(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('mainpage')
    else:
        form = UserUpdateForm(instance=request.user)
    context = { "form": form}
    return render(request, 'todo/settings.html', context)

# @login_require()
# def password_reset(request):
#     return render(request, 'registration/password_reset.html')