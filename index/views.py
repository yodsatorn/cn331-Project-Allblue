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

def menu(request):
	return  render(request, "menu.html")
	
#for user register
def register(request):
	if request.method == 'POST':
		
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')

		newuser = User.objects.create_user(username= username, password= password, email= email, first_name= first_name, last_name= last_name)

		newuser.save()
		
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