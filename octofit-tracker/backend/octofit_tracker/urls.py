"""octofit_tracker URL Configuration

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Dummy viewsets for demonstration (replace with real ones as needed)
from rest_framework import viewsets
from django.http import JsonResponse

class UsersViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([])

class TeamsViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([])

class ActivitiesViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([])

class WorkoutsViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([])

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([])

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'teams', TeamsViewSet, basename='teams')
router.register(r'activities', ActivitiesViewSet, basename='activities')
router.register(r'workouts', WorkoutsViewSet, basename='workouts')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
