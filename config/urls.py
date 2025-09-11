"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 기본 주소('/')로 접속하면 'pybo' 앱의 페이지로 바로 연결
    path('', include('pybo.urls')),
    path('pybo/', include('pybo.urls')),
    path('', views.index, name='index'),  # /  페이지에 해당하는 urlpattern
    path('common/',include('common.urls'))
]
