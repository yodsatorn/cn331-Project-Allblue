from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


# Create your views here.

def index(request):
	return  render(request, "index.html")

def about(request):
	return  render(request, "about.html")

def menu2(request):
	return  render(request, "menu2.html")

def menu3(request):
	return  render(request, "menu3.html")
	
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

		return redirect('index')

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
				"message": "Invalid Credentials"
			})

	return render(request, 'login.html')