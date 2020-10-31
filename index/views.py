from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')
		
		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		
		return HttpReponseRedirect('index')

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