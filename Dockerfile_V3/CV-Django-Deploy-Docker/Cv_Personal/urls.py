"""Cv_Personal URL Configuration

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
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('formacion_academica/', views.Shesst2_CV.as_view(), name='formacion_academica'),
    path('formacion_academica_ce/', views.Shesst3_CV.as_view(), name='formacion_academica_ce'),
    path('formacion_academica_ct/', views.Shesst4_CV.as_view(), name='formacion_academica_ct'),
    path('experiencia/', views.Shesst5_CV.as_view(), name='experiencia'),

    #path('skills/', include('skills.urls', namespace='skills')),
    path('', include('skills.urls')),
    path('', include('FormAcad.urls')),
    path('', include('FormEsp.urls')),
    path('', include('Certificados.urls')),
    path('', include('Experience.urls')),
    path('', include('actividad_adicional.urls')),


] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
