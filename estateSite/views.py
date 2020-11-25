from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from estate.forms.custom_form import CustomUserCreationForm


# def signup(request):
#     """Register a new user."""
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # username = form.cleaned_data.get('username')
#             # raw_password = form.cleaned_data.get('password')
#             # user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             # return redirect('estate:index')
#             return redirect('account_login')
#         else:
#             msg = f"Form is not valid"
#             messages.error(request, msg)
#             return HttpResponseRedirect(reverse('account_signup'))
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})
