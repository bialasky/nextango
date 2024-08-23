from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ItemViewSet, api_root

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', api_root, name='api_root'),  # Add this line for the root view
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]