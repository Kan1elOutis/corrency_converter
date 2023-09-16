from django.contrib import admin

from django.urls import path
from rest_framework.routers import SimpleRouter

from exchange_app.views import ConverterViewSet

router = SimpleRouter()

router.register(r'api/v1/', ConverterViewSet, basename='Converter')

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls