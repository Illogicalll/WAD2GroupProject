"""groupproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from resell import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('signupsuccess/', views.signupsuccess, name='signupsuccess'),
    path('loginsuccess/', views.loginsuccess, name='loginsuccess'),
    path('admin/', admin.site.urls),
    path('item/<int:product_id>', views.item, name='item'),
    path('profile/<int:profile_id>', views.profile, name='profile'),
    path('listings/', views.buy.as_view(), name='listings'),
    path('profile', views.myprofile, name='myprofile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('newlisting/', views.newlisting, name='newlisting'),
    path('listingsuccess/', views.listingsuccess, name='listingsuccess'),
    path('accounts/login/?next=/newlisting/', views.login, name='loginredirect'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

