from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # User with unique name
        if form.is_valid():
            # Save the user to db
            form.save()
            username = form.cleaned_data.get('username')
            # Show a success message to the user
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
