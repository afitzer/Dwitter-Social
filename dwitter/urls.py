from django.urls import path, include, re_path
from . import views

app_name = "dwitter"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
]