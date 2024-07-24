from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members_list, name='members_list'),
    path('members/add/', views.add_member, name='add_member'),
    path('events/', views.events_list, name='events_list'),
    path('donations/', views.donations_list, name='donations_list'),
]

# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
    path('member/new/', views.member_new, name='member_new'),
    path('member/<int:pk>/edit/', views.member_edit, name='member_edit'),
]
