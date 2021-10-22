from django.shortcuts import redirect, render
from django.contrib.auth import login as login_user, logout as logout_user
from .models import User, Journal

def homepage(request):
    return render(request, "homepage.html", {})


def login(request):
    if request.method == 'POST':
        context = {}
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
            if user.check_password(password):
                login_user(request, user)
            else:
                context['error'] = "Invalid login credentials"
            
        except User.DoesNotExist:
            context['error'] = "Invalid login credentials"
        
    return render(request, "login.html", context)


def register(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        email = request.POST.get('email')
        if password == repeat_password == False:
            context['error'] = "passwords do not match"
            return render(request, 'register.html', context)
        else:
            try:
                user = User()
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
                #login user
                login_user(request, user)
                return render(request, 'dash.html', context)
            except:
                context['error'] = "an error occured try again later"
        

def dash(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    context = {}
    user = request.user
    journals = Journal.objects.filter(user = user)
    context['journals'] = journals
    return render(request, 'dash.html', context)


def add_note(request):
    if request.user.is_authenticated == False:
        return redirect("login")

    if request.method == "POST":
        title = request.POST.get('title')
        user = request.user
        content = request.POST.get('content')
        j = Journal()
        j.title = title
        j.user = user
        j.content = content
        j.save()

def edit_note(request, note_id):
    if request.user.is_authenticated == False:
        return redirect("login")
    context = {}
    if request.method == "POST":
        try:
            j = Journal.objects.get(id = note_id)
            j.title = request.POST.get("title")
            j.content = request.POST.get("content")
            j.save()
            context['success'] = "the journal has been edited successfully"
            return render(request, 'dash.html', context)
        except:
            context['error'] = "an error occured while trying to edit the journal"
            return render(request, 'dash.html', context)
    
    return redirect('dash')

def delete_note(request, note_id):
    if request.user.is_authenticated == False:
        return redirect("login")
    context = {}
    user = request.user
    try:
        user.journal_set.get(id = note_id)
    except:
        context['error'] = "an error occured, the note could not be deleted"
        return render(request, 'dash.html', {})
    
    return redirect("dash")