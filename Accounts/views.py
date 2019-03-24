from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from Accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
def user_registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = form.save(commit=True)
            groups = form.cleaned_data.get('groups')
            for group in groups:
                user.groups.add(Group.objects.get(name = group))
            user.save()
            authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Account has been created for %s " % username)
            return redirect('Application:all-views')
    else:
        form = UserRegisterForm()
    return render(request, 'Accounts/user_registration_form.html', {'form': form})
