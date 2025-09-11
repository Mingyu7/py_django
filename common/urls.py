
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # 인증 모듈

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
]
