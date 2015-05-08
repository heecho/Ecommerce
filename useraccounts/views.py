from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from items.models import Order
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
	return render(request, 'useraccounts/home.html', {})

def sign_up(request):
	template_hash = {}
	return render(request,'useraccounts/signup.html',template_hash)
	#return HttpResponse('New User Sign-Up Page')

def register(request):
	print request.POST
	user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.save()
	if request.user.is_authenticated():
		login(request, user)
		return HttpResponseRedirect(reverse('items:index',))
	else:
		return HttpResponseRedirect(reverse('useraccounts:login'))

def show_user(request, user_id):
	user = User.objects.get(pk=user_id)
	if request.user.is_authenticated():
		template_hash = {'user': user}
		return render(request, 'useraccounts/showuser.html',template_hash)
	else:
		return HttpResponse('Login for Access')

def log_in(request):
	template_hash = {}
	return render(request,'useraccounts/login.html',template_hash)
	#return HttpResponse('Login')

def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password=password)
	if user is not None:
		login(request, user)
		order = Order.objects.filter(status=1, user_id = request.user.id)
		if not order:
			order = Order()
			order.status = 1
			order.user = request.user
			order.save()
		return HttpResponseRedirect(reverse('items:index',))
	else:
		return HttpResponse('invalid Login')
	#return HttpResponse('You can proceed')

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('home',))

def item_index(request):
	pass


