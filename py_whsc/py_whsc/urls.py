"""py_whsc URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from apps.admins.urls import Admin_router
from apps.books.urls import Book_router
from apps.config.urls import Banner_router

urlpatterns = [
    path('', admin.site.urls),
    path('ad/', include(Admin_router.urls)),
    path('book/', include(Book_router.urls)),
    path('ban/', include(Banner_router.urls)),
]
admin.sites.AdminSite.site_header = '网红书城管理系统'
admin.sites.AdminSite.site_title = '网红书城管理系统'
admin.sites.AdminSite.index_title = '网红书城管理系统'
