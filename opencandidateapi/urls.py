"""opencandidateapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from candidates.urls import router as candidate_router
from opinions.urls import router as opinion_router
from backups.urls import router as backup_router

router = DefaultRouter()
router.registry.extend(candidate_router.registry)
router.registry.extend(opinion_router.registry)
router.registry.extend(backup_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
