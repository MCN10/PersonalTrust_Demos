from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import *
from django.contrib import messages
from .models import *
from app.models import *

def registration_view(request):
	if request.user.is_authenticated:
	 	return redirect("app:home")

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			Customer.objects.create(
                    user=account,
                    email=email,
                )
			login(request, account)
			messages.success(request, ('Registration Successful'))
			return redirect('app:home')
		else:
			context['registration_form'] = form
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	messages.success(request, ("You have been logged out."))
	return redirect('account:login')


def login_view(request):

	 context = {}

	 user = request.user
	 if user.is_authenticated:
	 	return redirect("app:home")

	 if request.POST:
	 	form = AccountAuthenticationForm(request.POST)
	 	if form.is_valid():
	 		email = request.POST['email']
	 		password = request.POST['password']
	 		user = authenticate(email=email, password=password)

	 		if user:
	 			login(request, user)
	 			messages.success(request, ("Welcome back!"))
	 			return redirect("app:home")
	 		else:
	 			messages.success(request, ("Ooops! We're sorry but that didn't work. Please try again!"))
	 			return redirect('account:login')

	 else:
	 	form = AccountAuthenticationForm()

	 context['login_form'] = form
	 return render(request, 'account/login.html', context)
