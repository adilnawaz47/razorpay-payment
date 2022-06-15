# dj_razorpay/urls.py

from django.contrib import admin
from django.urls import path
from payment import views

urlpatterns = [
	path("", views.home, name="home"),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
	path('admin/', admin.site.urls),
]
