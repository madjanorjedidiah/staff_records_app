from django.test import TestCase, Client
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from auth_now.models import *


class ViewUsersTest(TestCase):


	def setUp(self):
		self.user = UserIdentity.objects.create(username='jedi')
		self.user.set_password('jed123456')
		self.user.save()
		self.client = Client()


	def test_sign_up(self):
		response = self.client.post(reverse('signup'), data={'username':'oko', 'password': 'oko123456', 'confirm_password': 'oko123456'})
		# user_n = UserIdentity.objects.create(username='jedi')
		# user_n.set_password('jed123456')
		# user_n.save()
		self.assertEqual(response['Location'], '/dashboard/')


	def test_sign_up_duplicate(self):
		try:
			user, created = UserIdentity.objects.get_or_create(username='jedi', password='jed123456')
			self.assertEqual(created, False)
		except Exception:
			pass


	def test_login(self):
		response = self.client.login(username = 'jedi', password = 'jed123456')
		self.assertEqual(response, True)


	def test_logout(self):
		response = self.client.get(reverse('logout'))
		self.assertEqual(response["Location"], "/")


	def test_user_bio(self):
		response = UserBioInfo.objects.create(
			title = 'title', 
			name = 'name',
			email = 'email',
			phone_number = 'phone_number',
			gender = 'gender', 
			department = 'department',
			last_cert_date = '2004-12-12', 
			image = 'image',
			user_fk_id = self.user.id
			)
		self.assertEqual(response.title, 'title')
	