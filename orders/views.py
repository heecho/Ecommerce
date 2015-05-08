from django.shortcuts import render
from items.models import Item, Order
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
	user = request.user
	print user
	order = Order.objects.filter(status=1, user_id=user.id)
	print order
	print user.id
	if not order:
		template_hash={'order_items':[] ,'total': 0}
		return render(request, 'orders/index.html',template_hash)
	order_items = order[0].items.all()
	print order_items
	total = 0
	for item in order_items:
		total += item.price
	template_hash = {'order_items':order_items, 'total':total}
	if user.is_authenticated():
		return render(request, 'orders/index.html',template_hash)
	else:
		return HttpResponseRedirect(reverse('useraccounts:login',))
	#return HttpResponse('this is your cart')

def deleteitem(request,item_id):
	user = request.user
	order = Order.objects.filter(status=1, user_id=user.id)
	order[0].items.remove(Item.objects.get(pk=item_id))
	return HttpResponseRedirect(reverse('orders:index',))

def payment(request):
	user = request.user
	order = Order.objects.filter(status=1, user_id=user.id)
	order_id = order[0].id
	template_hash = {'order_id':order_id}
	return render(request,'orders/payment.html', template_hash)
	#return HttpResponse('Payment Form')

def processed(request,order_id):
	user = request.user
	order = Order.objects.filter(status=1, pk=order_id, user_id = user.id)[0]
	order.status = 2
	order.save()
	# neworder = Order()
	# order.status = 1
	# order.user = user
	# order.save()
	return HttpResponseRedirect(reverse('items:index',))
