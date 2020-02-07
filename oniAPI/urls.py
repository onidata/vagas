"""oniAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#include essential libraries
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

#include project apps
from contracts.urls import urlpatterns as contracts
from users.urls import urlpatterns as users
from payments.urls import urlpatterns as payments


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include_docs_urls(title='Onidata Project API')),
    path('token/', TokenObtainPairView.as_view(), name='token_get_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += contracts
urlpatterns += users
urlpatterns += payments
