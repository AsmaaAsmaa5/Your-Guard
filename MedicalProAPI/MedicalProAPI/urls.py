"""
URL configuration for MedicalProAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyApp import views,backends

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('api/Tips/', views.TipsListCreateAPIView.as_view(), name='Tips-list-create'),
    path('api/Tips/<int:pk>/', views.TipsRetrieveUpdateDestroyAPIView.as_view(), name='Tips-retrieve-update-destroy'),
    path('api/friends/', views.FriendListCreateAPIView.as_view(), name='friend-list-create'),
    path('api/friends/<int:pk>/', views.FriendRetrieveUpdateDestroyAPIView.as_view(), name='friend-retrieve-update-destroy'),
    path('api/emergencies/', views.EmergencyListCreateAPIView.as_view(), name='emergency-list-create'),
    path('api/emergencies/<int:pk>/', views.EmergencyRetrieveUpdateDestroyAPIView.as_view(), name='emergency-retrieve-update-destroy'),
    path('api/videos/', views.VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('api/videos/<int:pk>/', views.VideoRetrieveUpdateDestroyAPIView.as_view(), name='video-retrieve-update-destroy'),
    path('api/coaches/', views.CoachListCreateAPIView.as_view(), name='coach-list-create'),
    path('api/coaches/<int:pk>/', views.CoachRetrieveUpdateDestroyAPIView.as_view(), name='coach-retrieve-update-destroy'),
    path('api/hospitals/', views.HospitalListCreateAPIView.as_view(), name='hospital-list-create'),
    path('api/hospitals/<int:pk>/', views.HospitalRetrieveUpdateDestroyAPIView.as_view(), name='hospital-retrieve-update-destroy'),
    path('api/payments/', views.PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('api/payments/<int:pk>/', views.PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-retrieve-update-destroy'),
    path('api/login/', views.login, name='login'),
    path('api/signup/', views.signup, name='signup'),
]