
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # 인증 모듈

from common import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),

]
