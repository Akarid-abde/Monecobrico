from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('service/<slug:slug>/', views.ServiceDetail, name="service"),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]
