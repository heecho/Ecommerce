from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Ecomm.views.home', name='home'),
    url(r'^$', 'useraccounts.views.home', name = 'index'),
    url(r'^signup$', 'useraccounts.views.sign_up', name='new'),
	url(r'^register$', 'useraccounts.views.register', name='create'),
	url(r'^(?P<user_id>[0-9]+)/?$', 'useraccounts.views.show_user', name='showuser'),
	url(r'^login$', 'useraccounts.views.log_in', name='login'),
	url(r'^login_user$', 'useraccounts.views.login_user', name='login_user'),
	url(r'^logout$', 'useraccounts.views.log_out', name='logout'),
	]