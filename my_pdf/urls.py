"""my_pdf URL Configuration

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
from blanks import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static


urlpatterns = [
    path('', views.Home, name='Home'),
    path('edit_files/', views.edit_files,name='edit_files' ),
    path('files/', views.file_list, name='file_list'),
    path('upload_files/', views.upload_files, name="upload_files"),
    path('admin/', admin.site.urls),
    path('files/<int:pk>/', views.delete_book, name='delete_book'),
    path('my_blanks/<int:file_id>/', views.edit_files, name='edit_files'),
    path('signup/',views.signup,  name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('settins/', views.settins, name='settins')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)