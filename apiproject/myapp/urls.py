from django.urls import path
from myapp import views

urlpatterns = [
    # path('myapi/', views.BlogList.as_view()),
    # path('detail/<int:pk>/', views.ApiDetails.as_view()),
    path('generic_api_view/', views.ContactList.as_view()),
    path('mydetail/<int:pk>/', views.ContactDetail.as_view())
]