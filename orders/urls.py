from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'Ecomm.views.home', name='home'),
    url(r'^$', 'orders.views.index', name = 'index'),
	url(r'^(?P<item_id>[0-9]+)/deleteitem/?$', 'orders.views.deleteitem', name='deleteitem'),
	url(r'^payment$', 'orders.views.payment', name='payment'),
	url(r'^(?P<order_id>[0-9]+)/processed$', 'orders.views.processed', name='processed')
	]