from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from recipes.models import Recipes
from django.db import IntegrityError

# Create your views here.

def index(request):
	return  render(request, "index.html")

def about(request):
	return  render(request, "about.html")

#for user register
def register(request):
	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		
		try:
			if User.objects.filter(email = email).exists() :
				raise IntegrityError('Email was taken.')
			elif User.objects.filter(username = username).exists() :
				raise IntegrityError('Username was taken.')

			newuser = User.objects.create_user(username= username, password= password, email= email, first_name= first_name, last_name= last_name)
			newuser.save()

		except IntegrityError as e:
			return render(request, 'register.html',{
				'error_message' : e
			})

		return redirect('login')

	return render(request, 'register.html')

def view_login(request):

	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username= username, password= password)
		if user is not None:
			login(request, user)
			return redirect("index")
		else :
			return render(request, "login.html", {
				"error_message": "Invalid Credentials"
			})

	return render(request, 'login.html')

def view_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def profile(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	return render(request,"profile.html", {
		"user_id":request.user.id,
		}
	)

def editProfile(request):
	if request.method == 'POST':
		if request.user.is_authenticated:
			user = User.objects.get(username=request.user.username)
			user.set_password(request.POST.get('password'))
			user.first_name = request.POST.get('first_name')
			user.last_name = request.POST.get('last_name')
			user.save()
			user = authenticate(request, username= request.user.username, password= request.POST.get('password'))
			login(request, user)
		return redirect("profile")
	else:
		
		return render(request,"editProfile.html")
	