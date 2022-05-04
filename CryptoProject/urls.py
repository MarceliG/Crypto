from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from CryptoAplication.views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("CryptoAplication.urls")),
    path("django_plotly_dash/", include("django_plotly_dash.urls")),
    path('rest/', include(router.urls)),
]
