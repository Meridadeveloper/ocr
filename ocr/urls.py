"""
URL configuration for ocr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from ocr_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/c',TranslatePDFAPIView.as_view(),name='TranslatePDFAPIView'),
    # path('api/generate_content/',generate_content,name='generate_content'),

    path('api/generate_content/',GenerateContentView.as_view(),name='generate_content_class'),

    path('RegistrationView/',RegistrationView.as_view(),name='RegistrationView'),
    path('StudiesListView/',StudiesListView.as_view(),name='StudiesListView'),
    

    
] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
