from django.test import TestCase, Client
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from auth_now.models import *


class ViewUsersTest(TestCase):


	def setUp(self):
		self.client = Client()


	def test_sign_up(self):
		user = UserIdentity.objects.create(username='jedi', password='jed123456')
		self.assertEqual(user.username, 'jedi')


	def test_sign_up_duplicate(self):
		user, created = UserIdentity.objects.get_or_create(username='jedi', password='jed123456')
		self.assertEqual(created, True)


	def test_login(self):
		response = self.client.post(reverse('login'), {'username':'jedi', 'password':'jed123456'})
		self.assertTemplateUsed(response, 'dashboard.html')


	def test_logout(self):
		response = self.client.get(reverse('logout'))
		self.assertTemplateUsed(response, 'index.html')


	def test_user_bio(self):
		response = self.client.post(reverse('userbio', {
			'title':'title', 
			'name':'name',
			'gender':'gende', 
			'department':'department',
			'last_cert_date':'last_cert_date', 
			'image':'image',
			}
			))
		self.assertTemplateUsed(response, 'userbio.html')
	