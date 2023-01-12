from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.BlogList.as_view()),
    path('detail/<int:pk>/', views.ApiDetails.as_view()),
]