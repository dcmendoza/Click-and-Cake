from django.shortcuts import render
from django.contrib.auth.hashers import make_password

# Create your views here.
def save(self, *args, **kwargs):
		"""
		Overriding save method to ensure that passwords are hashed before saving the Account object.
		"""
		if self._state.adding and self.password:  # Only hash on account creation or password change
			self.password = make_password(self.password)
		super().save(*args, **kwargs)

user = User.objects.create_user(username=username, password=password)