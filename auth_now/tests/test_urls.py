from django.test import TestCase
from auth_now.views import *
from django.urls import reverse, resolve




class UrlsUsersTest(TestCase):
	
	def test_sign_up_url(self):
		resolver = resolve(reverse('signup'))
		self.assertEqual(resolver.func, signup)


	def test_dashboard_url(self):
		resolver = resolve(reverse('dashboard'))
		self.assertEqual(resolver.func, dashboard)


	def test_login_url(self):
		resolver = resolve(reverse('login'))
		self.assertEqual(resolver.func, login_view)


	def test_logout_url(self):
		resolver = resolve(reverse('logout'))
		self.assertEqual(resolver.func, logout_view)
		