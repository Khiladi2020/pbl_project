from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Create your views here.

def welcome(request):
	return HttpResponse("Welcome to AIT Food Waste Management App")

def test(request):
	return JsonResponse({'hi':'hmm'})

@csrf_exempt
def signup_user(request):
	try:
		u_username=request.POST['username']
		u_password=request.POST['password']
		u_email=request.POST['email']
		u_fname=request.POST['firstname']
		u_lname=request.POST['lastname']

		user = User.objects.create_user(
			username = u_username,
			password= u_password,
			email=u_email,
			first_name = u_fname,
			last_name=u_lname
		)
		user.save()
		return JsonResponse({'status':'new user created successfully'})
	except:
		return JsonResponse({'status':'failed to create user'})

# @csrf_exempt
def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('main_app:vote')
		# data = {
		# 	'status':'logged in'
		# }
		# return JsonResponse(data)
	else:
		# data = {
		# 	'status':'invalid credentials'
		# }
		# return JsonResponse(data)
		return redirect('main_app:vote')

@csrf_exempt
def logout_user(request):
	logout(request)
	return redirect('main_app:vote')

def home(request):
	return render(request,'main_app/index.html',{})

def daily_waste(request):
	return render(request,'main_app/daily_waste.html',{})

def stats(request):
	return render(request,'main_app/statistics.html',{})

def vote(request):
	return render(request,'main_app/voting.html',{})

def awareness(request):
	return render(request,'main_app/awareness.html',{})

def contact(request):
	return render(request,'main_app/contact_us.html',{})
