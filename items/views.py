from django.shortcuts import render
from django.core import serializers
from django.db.models import Q
from .models import Item, Order
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
	user = request.user
	search_term = request.GET.get('search')
	price_filter = request.GET.get('price')
	print price_filter
	
	price_hash = {'1':Item.objects.filter(price__lte = 50),
		'2':Item.objects.filter(price__gte = 51).filter(price__lte = 100),
		 '3':Item.objects.filter(price__gte = 101).filter(price__lte = 500),
		 '4':Item.objects.filter(price__gte = 501) }
	
	if search_term:
		item_list = Item.objects.filter(Q(name__icontains = search_term) | Q(description__icontains = search_term))
	elif price_hash.has_key(price_filter):
		item_list = price_hash[price_filter]
	else:
		item_list = Item.objects.all()

	paginator = Paginator(item_list, 10)
	page = request.GET.get('page')

	try:
		items_page = paginator.page(page)
	except PageNotAnInteger:
		items_page = paginator.page(1)
	except EmptyPage:
		items_page = paginator.page(paginator.num_pages)
	
	template_hash = {'page': page, "items_page":items_page, 'user':user}
	
	if request.GET.get('format') == 'json':
		data = serializers.serialize("json", items_page)
		return HttpResponse(data, content_type='application/json') 
	else:
		return render(request,'items/index.html', template_hash)
	#return HttpResponse('item index')

def show_item(request, item_id):
	item = Item.objects.get(pk=item_id)
	template_hash = {'item':item}
	return render(request, 'items/show.html',template_hash)

def additem(request,item_id):
	user = request.user
	print user
	if user.is_authenticated():
		order = Order.objects.filter(status=1, user_id = user.id)
		if order:
			print item_id
			order[0].items.add(Item.objects.get(pk=item_id))
			return HttpResponseRedirect(reverse('orders:index',))
		else:
			order = Order()
			order.status = 1
			order.user = user
			order.save()
			order.items.add(Item.objects.get(pk=item_id))
			return HttpResponseRedirect(reverse('orders:index',))
		#return HttpResponseRedirect(reverse('orders:index', args=(order.id,)))
	else:
		return HttpResponseRedirect(reverse('useraccounts:login',))
		#redirect to login page


