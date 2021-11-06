from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm

User = get_user_model()

@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            #
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
@require_http_methods(['POST', 'GET'])
def update(request):
    user = request.user
    if request.method == 'POST':
      #
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            #
            user = form.save()
            return redirect('accounts:profile', user.username)
    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['POST', 'GET'])
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:profile', user.username)
    else:
        form = PasswordChangeForm(user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

@require_POST
def delete(request):
    user = request.user
    if user.is_authenticated:
        user.delete()
    return redirect('articles:index')


@require_http_methods(['POST', 'GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_safe
def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)