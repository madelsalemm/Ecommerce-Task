from django.urls import path , include
from . import views
from knox import views as knox_views
app_name = 'account'

urlpatterns = [
    path('signup/', views.signup , name="signup" ),
    ################# api ############
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    ################# api ############
    
]