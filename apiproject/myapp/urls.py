from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.api_list),
    path('api_details/<int:pk>/', views.api_details),
]