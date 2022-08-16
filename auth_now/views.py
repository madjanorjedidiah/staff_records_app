from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import UserBioForm
from .helpers import add_user_id_n_save, get_user


def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		if password == confirm_password:
			user, created = UserIdentity.objects.get_or_create(username=username.lower())
			if created:
				user.set_password(password)
				user.save()
				messages.add_message(
					request, 
					messages.INFO,
					"You have successfully signed up",
					extra_tags = 'success')
				return render(request, 'auth_now/dashboard.html')
			messages.add_message(
				request,
				messages.INFO,
				'User already exists',
				extra_tags = 'danger')
	return render(request, 'auth_now/signup.html')


# ##################   Login view   ##########################################
def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =  request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'auth_now/dashboard.html')
		else:
			return HttpResponse('error')		
	return render(request, 'auth_now/login.html')


# ##################   Logout view   ##########################################
def logout_view(request):
	logout(request)
	# return HttpResponseRedirect(reverse('home'))
	return render(request, 'auth_now/index.html')


def index(request):
	return render(request, 'auth_now/index.html')


def dashboard(request):
	return render(request, 'auth_now/dashboard.html')


def admin_level(request):
	return render(request, 'auth_now/admin.html', {'data':UserBioInfo.objects.all()})


def userbio(request):
	if request.method == 'POST':
		form = UserBioForm(request.POST)
		if form.is_valid():
			add_user_id_n_save(request, form, unique=True)
			messages.add_message(
				request, 
				messages.INFO,
				"You have successfully submitted your record",
				extra_tags = 'success'
			)
	return render(request, 'auth_now/userbio.html')