# from django.urls import path
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename = 'products')
router.register('categories', CategoryViewSet, basename = 'categories')


urlpatterns = router.urls



#urlpatterns = [
#    path('products/', ProductList.as_view(), name='product-list'),
#    path('products/<int:pk>', ProductDetail.as_view(), name='product-detail'),
 #]
