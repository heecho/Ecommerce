from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Ecomm.views.home', name='home'),
    url(r'^$', 'items.views.index', name = 'index'),
	url(r'^(?P<item_id>[0-9]+)/?$', 'items.views.show_item', name='showitem'),
	url(r'^(?P<item_id>[0-9]+)/additem/?$', 'items.views.additem', name='additem'),
	
	]