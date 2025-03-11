from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password using set_password to hash it
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object to the database
            new_user.save()
            # Render the registration done template
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        # If GET request, display an empty form
        user_form = UserRegistrationForm()
    
    return render(request, 'registration/signup.html', {'user_form': user_form})





@login_required
def profile_details(request):
    user = request.user
    return render(request, 'registration/profile_details.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        # If the user provided a new password, update it
        password = request.POST.get('password')
        if password:
            user.set_password(password)

        user.save()

        # Update session authentication hash to keep the user logged in after password change
        update_session_auth_hash(request, user)

        return redirect('/')
    
    return render(request, 'registration/edit_profile.html')