from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from accounts.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)


        return redirect('/')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)


def logout_request(request):
    logout(request)
    return redirect(reverse('Login') + '?mensaje=Sesión + cerrada.')

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)


@login_required
def editar_request(request):
    user = request.user
    if request.method == "POST":

        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.save()
        return redirect("/")

    form = UserUpdateForm(initial={"username": user.username, "email": user.email})
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)

@login_required
def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":

        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user=user,
                    imagen=data["imagen"]
                )
            avatar.save()

            return redirect("/")

    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)