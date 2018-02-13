"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from myapp.views import register
from myapp.views import login
from myapp.views import logout
from myapp.views import gameq2clone
from myapp.views import gameq4clone
from myapp import views as v1
from myapp.views import gameq4


from myapp.views import gameq4

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'register/',register),
    path(r'login/',login),
    path(r'gameq2clone/',gameq2clone),
    path(r'gameq4clone/',gameq4clone),
    path(r'logout/',logout),
    path(r'gameq2turn/',v1.gameq2.turn),
    path(r'gameq2is_end/',v1.gameq2.is_end),
    path(r'gameq2isvalidplayer/',v1.gameq2.isvalidplayer),
    path(r'gameq2isvalidvwall/',v1.gameq2.isvalidvwall),
    path(r'gameq2isvalidhwall/',v1.gameq2.isvalidhwall),
    path(r'gameq2havewall/',v1.gameq2.havewall),
    path(r'gameq2pluswall/',v1.gameq2.pluswall),
    path(r'gameq4/',gameq4)
]
