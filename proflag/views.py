from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from .forms import UserProfileForm

def register_request(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)

		if form.is_valid():
			user = form.save(commit=True)
			user.save()

			login(request, user)
			messages.success(request, "Registration successful.")
			
			return redirect("/")
		
		return render(request, "registration/register.html", {"form": form})
		
	form = UserCreationForm()
	form.fields['username'].widget.attrs['placeholder'] = "Username"
	form.fields['password1'].widget.attrs['placeholder'] = "Password"
	form.fields['password2'].widget.attrs['placeholder'] = "Password confirmation"
	
	return render(request, "registration/register.html", {"form": form})

@login_required
def profile_request(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			user = form.save(commit=True)
			user.save()

			return redirect("/")
		
		return render(request, "registration/profile.html", {"form": form})
		
	form = UserProfileForm(instance=request.user)
	form.fields["username"].widget.attrs['placeholder'] = "Username"

	return render(request, "registration/profile.html", {"form": form})

@login_required
def change_password(request):
	if request.method == "POST":
		form = AdminPasswordChangeForm(user=request.user, data=request.POST)

		if form.is_valid():
			user = form.save(commit=True)
			user.save()

			login(request, user)

			return redirect("/")
		
		return render(request, "registration/change_password.html", {"form": form})
	
	form = AdminPasswordChangeForm(user=request.user)
	form.fields['password1'].widget.attrs['placeholder'] = "Password"
	form.fields['password2'].widget.attrs['placeholder'] = "Password confirmation"

	return render(request, "registration/change_password.html", {"form": form})