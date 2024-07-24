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
    path('', views.home, name='home'),
    path('members/', views.member_list, name='member_list'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
    path('member/new/', views.member_new, name='member_new'),
    path('member/<int:pk>/edit/', views.member_edit, name='member_edit'),
]

# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/new/', views.event_create, name='event_create'),
    path('events/<int:pk>/edit/', views.event_update, name='event_update'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),
]


urlpatterns += [
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/new/', views.donation_create, name='donation_create'),
    path('donations/<int:pk>/edit/', views.donation_update, name='donation_update'),
    path('donations/<int:pk>/delete/', views.donation_delete, name='donation_delete'),
]
