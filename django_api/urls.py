from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from rest_framework import routers
from . import settings
from groups import views

router = routers.DefaultRouter()
router.register('elements', views.ElementViewSet)
router.register('groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('groups/<int:pk>/child_groups/', views.ChildGroupViewSet.as_view({'get': 'list'}), name='child-groups'),
    path('elements/<int:pk>/child_elements/', views.ChildElementViewSet.as_view({'get': 'list'}), name='child-elements')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

