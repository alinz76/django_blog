from pyexpat import model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')

            return redirect('user-login')
        
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.user.is_authenticated:
            messages.info(request, "You have successfully logged out.")
        return response
    

class UserLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if request.user.is_authenticated:
            messages.success(request, "Welcome To My Website!")
        return response
    

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('user-profile', username)

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'user': user,
        'u_form' : u_form,
        'p_form' : p_form,
        'posts' : posts,
    }
    return render(request, 'users/profile.html', context)