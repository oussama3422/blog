from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from users.models import Profile
from .form import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.') 
            return redirect('login') #redirect them im login page
        else:
            print(form.errors)  # Add this line to print errors to the console
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# def register(request):
#     # check if the request method is POST request
#     if request.method == "POST":
#         form=UserRegisterForm(request.POST)
#         # check if the form is valid
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             messages.success(request,f'Account created for {username}!')
#             return redirect('blog')
#     else:
#         form=UserRegisterForm()
#     return render(request,'users/register.html',{'form':form})



# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('home')  # Change 'blog' to the name of your home or blog URL pattern
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('blog')



@login_required
def profile(request):
    try:
        # Attempt to get the Profile instance, if it exists
        profile_instance = request.user.profile
    except Profile.DoesNotExist:
        # If the Profile instance does not exist, create a new one
        profile_instance = Profile(user=request.user)
        profile_instance.save()

    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=profile_instance)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_instance)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile.html', context)
