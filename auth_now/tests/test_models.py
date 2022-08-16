from django.test import TestCase
from auth_now.models import *


class ModelUsersTest(TestCase):


	def test_users_model(self):
		self.assertEqual(str(UserIdentity._meta.verbose_name), 'user')


	def test_users_bio_model(self):
		self.assertEqual(str(UserBioInfo._meta.verbose_name), 'user bio info')
	
	