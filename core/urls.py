from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.urls import path, include
from .api import views as viewsAPI
from . import views

router = DefaultRouter()
router.register(r'', viewsAPI.CitationViewSet, basename="citation")

urlpatterns = [
    path('citation/', include(router.urls)),
    path('', views.CitationListView.as_view(), name='citation'),
    path('officer/', views.Officer.as_view(), name='officer'),
    path('signup/', views.OfficerCreate.as_view(), name='signup'),
    path('officer/delete/<int:pk>/', views.OfficerDelete.as_view(), name='officer_delete'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)