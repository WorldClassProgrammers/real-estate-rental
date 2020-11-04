from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('estate:index')
            return redirect('login')
        else:
            msg = f"Form is not valid"
            messages.error(request, msg)
            return HttpResponseRedirect(reverse('signup'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
