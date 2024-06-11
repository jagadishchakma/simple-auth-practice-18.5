from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignUp, name="signup"),
    path('login/', views.UserLogin, name="login"),
    path('profile/', views.UserProfile, name="profile"),
    path('logout/', views.UserLogout, name='logout'),
    path('passchange/', views.UserPassChange, name='pass_change'),
    path('passchange2/', views.UserPassChange2, name='pass_change2'),
]
