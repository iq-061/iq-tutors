"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from core.views.home import home
from core.views.courses import courses
from core.views.about import about
from core.views.contact import contact
from core.views.pricing import pricing
from core.views.portal import portal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name = 'home'),
    path('home/', home, name = 'altHome'),
    path('courses/', courses, name = 'courses'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('pricing/', pricing, name = 'pricing'),
    path('portal', portal, name = 'portal')
]
