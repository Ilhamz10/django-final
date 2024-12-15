"""
URL configuration for core project.

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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail-service/', detail_service, name='detail'),
    path('our-blog/', our_blog, name='our_blog'),
    path('faq/', faq, name='faq'),
    path('our_team/', ourteam, name='our_team'),
    path('tac/', tac, name='tac'),
    path('detail-blog/<int:id>/', detail_blog, name='detail_blog'),
    path('about-us/', about_us, name='about_us'),
    path('', home_page, name='home'),
    path('our-service/', our_service, name='our_service')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)