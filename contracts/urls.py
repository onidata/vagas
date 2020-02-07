from rest_framework.routers import DefaultRouter
from contracts.views import ContractViewSet


router = DefaultRouter()
router.register(r'contracts', ContractViewSet)
urlpatterns = router.urls
