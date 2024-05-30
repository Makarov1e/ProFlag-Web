from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ("username",)
		exclude = ("date_joined",)