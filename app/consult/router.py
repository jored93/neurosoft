from rest_framework.routers import DefaultRouter
from app.consult.views import GraphEcgViewSet


router = DefaultRouter()
router.register('graph_ecg', GraphEcgViewSet, basename='graph_ecg')

urlpatterns = router.urls