from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # Show a success message to the user
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        # Create an empty form blank form with some sort of style
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
