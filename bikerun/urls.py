from django.urls import path, include
from . import views
app_name = 'bikerun'
urlpatterns = [
	path('',views.index, name = 'index'),
	path('contact/',views.contact, name = 'contact'),
	path('products/',views.products, name = 'products'),
]
