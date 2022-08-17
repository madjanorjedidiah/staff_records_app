from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import UserBioForm
from .helpers import add_user_id_n_save, get_user, remove_key_from_queryset, check_mutable, querydict_to_dict
from django.contrib.auth.decorators import login_required



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
				return HttpResponseRedirect(reverse('dashboard'))
			messages.add_message(
				request,
				messages.INFO,
				'User already exists',
				extra_tags = 'danger')
		messages.add_message(
				request,
				messages.INFO,
				'Passwords do not match',
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
			return HttpResponseRedirect(reverse('dashboard'))	
		messages.add_message(
				request,
				messages.INFO,
				'Incorrect credentials',
				extra_tags = 'danger')	
	return render(request, 'auth_now/login.html')


# ##################   Logout view   ##########################################
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


def index(request):
	return render(request, 'auth_now/index.html')


@login_required(login_url="/login/")
def dashboard(request):
	role_dict = {}
	data_table = UserBioInfo.objects.all()
	distinct_roles = data_table.values_list('role', flat=True).distinct()
	count_roles = [role_dict.update({a:data_table.filter(role=a).count()}) for a in distinct_roles]
	count_female = len(data_table.filter(gender='female'))
	count_male = len(data_table.filter(gender='male'))
	if len(data_table) > 3:
		
	context = {'role':role_dict, 'data_table':data_table, 'count_female':count_female, 'count_male':count_male}
	return render(request, 'auth_now/dashboard.html', context)


@login_required(login_url="/login/")
def admin_level(request):
	return render(request, 'auth_now/admin.html', {'data':UserBioInfo.objects.all()})


@login_required(login_url="/login/")
def profile(request):
	user = UserBioInfo.objects.filter(user_fk__username=request.user)
	return render(request, 'auth_now/profile.html', {'data':user[0] if user else None})


@login_required(login_url="/login/")
def userbio(request):
	if request.method == 'POST':
		form = UserBioForm(request.POST)
		new_data = check_mutable(request.POST, image=request.FILES.get(
            'image', None), user_fk_id=get_user(request).id)
		if form.is_valid() and 'image' in new_data:
			data, created = UserBioInfo.objects.get_or_create(
				user_fk_id=get_user(request).id,
                defaults = dict(querydict_to_dict((remove_key_from_queryset(new_data, 'csrfmiddlewaretoken')))),)
			if created:
				messages.add_message(
					request, 
					messages.INFO,
					"You have successfully submitted your record",
					extra_tags = 'success'
				)
		else:
			messages.add_message(
				request, 
				messages.INFO,
				form.errors,
				extra_tags = 'danger'
			)
	return render(request, 'auth_now/userbio.html')