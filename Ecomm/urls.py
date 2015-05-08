from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'useraccounts.views.home', name='home'),
    url(r'^accounts/', include('useraccounts.urls', namespace = 'useraccounts')),
    url(r'^items/', include('items.urls', namespace = 'items')),
    url(r'^cart/', include('orders.urls', namespace = 'orders')),
	url(r'^admin/', include(admin.site.urls)),
]
