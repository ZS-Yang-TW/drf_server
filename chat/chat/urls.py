from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from musics import views

router = DefaultRouter()
router.register('music', views.MusicViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("chatapi/", include("chatapi.urls")),
]