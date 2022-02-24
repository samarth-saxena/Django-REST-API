from django.urls import path
from . import views

urlpatterns = [
	path('', views.getAllRecords),
	path('create/', views.createRecords),
]