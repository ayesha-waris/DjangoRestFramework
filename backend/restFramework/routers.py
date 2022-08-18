from rest_framework.routers import DefaultRouter


from projects.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('product-abc', ProductGenericViewSet,
basename='products')
urlpatterns = router.urls
