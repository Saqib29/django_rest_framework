from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    # path('myapi/', views.BlogList.as_view()),
    # path('detail/<int:pk>/', views.ApiDetails.as_view()),
    path('generic_api_view/', views.ContactList.as_view(), name='contact-list'),
    path('mydetail/<int:pk>/', views.ContactDetail.as_view()),
    path('', views.api_root)
])