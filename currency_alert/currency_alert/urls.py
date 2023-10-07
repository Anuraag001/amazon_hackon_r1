"""
URL configuration for currency_alert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Main.views import front,signup,currency,send_Mail,convert,alert,create_alert,screen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',front,name="front"),
    path('signup/',signup,name='signup'),
    path('currency/<int:user_id>',currency,name='currency'),
    path('send_mail/',send_Mail,name='send_Mail'),
    path('convert/<int:user_id>',convert,name='convert'),
    path('alert/',alert,name='alert'),
    path('create_alert/',create_alert,name='create_alert'),
    path('screen/',screen,name="screen"),
]
