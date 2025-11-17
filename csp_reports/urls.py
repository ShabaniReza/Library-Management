from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('csp-reports', views.CspReportViewSet)

urlpatterns = router.urls