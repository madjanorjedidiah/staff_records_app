from . import views
from django.urls import path



urlpatterns = [
	path('', views.index, name='home'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('login/', views.login_view, name='login'),
	path('signup/', views.signup, name='signup'),
	path('logout/', views.logout_view, name='logout'),
	path('admin_level/', views.admin_level, name='admin_level'),
	path('userbio/', views.userbio, name='userbio'),
	path('profile/', views.profile, name='profile'),
	]