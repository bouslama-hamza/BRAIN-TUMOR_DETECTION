from django.urls import path , include
from django.contrib.auth.views import LoginView , LogoutView
from . import views
from .forms import UserLoginForm
from .list import ModelAPIView

urlpatterns = [
    path('' , LoginView.as_view(
                        template_name='login.html' , 
                            authentication_form=UserLoginForm
                                ) , name='client-login'
            ),
    path('logout/' , LogoutView.as_view(
                        next_page='client-login'
                                ) , name='client-logout'),
    path('signup/' , views.client_signup , name='client-signup'),
    path('dashboard/' , views.client_dashboard , name='client-dashboard'),
    path('api/model' , ModelAPIView.as_view() , name='client-api'),
]