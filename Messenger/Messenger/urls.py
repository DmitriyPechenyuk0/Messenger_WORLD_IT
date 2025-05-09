"""
URL configuration for Messenger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import settings
from authorization_app.views import AuthorizationView, LogoutView
from registration_app.views import RegistrationView
from home_app.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='registration/', view=RegistrationView.as_view(), name='reg'),
    path(route='authorization/', view=AuthorizationView.as_view(), name='auth'),
    path(route='log-out/', view=LogoutView.as_view(), name='logout'),
    path(route='', view=HomeView.as_view(), name='home' ),
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)