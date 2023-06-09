"""base URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import home, about_us, services, terms_of_service, privacy_policy, profile
from course.views import courses, course, enroll, quiz, leaderboard
from group.views import groups, group, join_group

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', home, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('services/', services, name='services'),
    path('terms-of-service/', terms_of_service, name='terms-of-service'),
    path('privacy_policy/', privacy_policy, name='privacy-policy'),
    path('profile/', profile, name='profile'),

    path('courses/', courses, name='courses'),
    path('courses/<int:pk>/', course, name='course'),
    path('courses/enroll/<int:pk>/', enroll, name='enroll'),
    path('courses/quiz/<int:pk>/', quiz, name='quiz'),
    path('courses/leaderboard/<int:pk>/', leaderboard, name='leaderboard'),

    path('groups/', groups, name='groups'),
    path('groups/<int:pk>/', group, name='group'),
    path('groups/join/<int:pk>/', join_group, name='join-group'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
