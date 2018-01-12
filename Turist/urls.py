"""Turist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from TuristManagment.views import index,contact,room,room_details,reservation,todo,booking,about

urlpatterns = [

    url(r'^$', index, name='index_page'),
    url(r'^contact/', contact, name='contact'),
    url(r'^todo/', todo, name='todo'),
    url(r'^reservation/', reservation, name='reservation'),
    url(r'^admin/', admin.site.urls),
    url(r'^Room/', room, name='room_page'),
    url(r'^about/', about, name='about_page'),
    url(r'^booking/', booking, name='booking'),


    url(r'^room/(?P<pk>[0-9]+)/$', room_details,name='room_details'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
