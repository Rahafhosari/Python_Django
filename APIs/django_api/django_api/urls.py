"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from django.conf.urls import url
import djangoapi.views
import djangoapi.api_views

# from django.views.generic import TemplateView
# from djangoapi import endpoints


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('djangoapi.urls')),
    path('api-auth/', include('rest_framework.urls')),

    #________ API Routes ________#
    path('api/v1/people',djangoapi.api_views.PersonList.as_view()),
    path('api/v1/people/new',djangoapi.api_views.PersonCreate.as_view()),
    # path('api/v1/people/<int:id>/destroy',djangoapi.api_views.PersonDestroy.as_view()),
    ##refactored url for destroy and update
    path('api/v1/people/<int:id>/',djangoapi.api_views.PersonRetrieveUpdateDestroy.as_view()),



    # url(r'^api/', include(endpoints)),
    # url(r'^', TemplateView.as_view(template_name="index.html")),
]
