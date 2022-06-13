"""restProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from app.api import UserAPI
from rest_framework.authtoken import views
from  app.views import Login, _redirect,Logout
from  rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView, # todo esto es lo importante como confguracion de jwt 
)


urlpatterns = [
    path("", _redirect),
    path('admin/', admin.site.urls),
    path('api/1.0/create_user/',UserAPI.as_view(),name='api_create_user'),
    path('api/1.1/',include(('app.url', 'apii'))),
    path('api_generate_token/',views.obtain_auth_token),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'), # todo esto es lo importante como confguracion de jwt 
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'), # todo esto es lo importante como confguracion de jwt 
]