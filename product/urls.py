from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    ProductViewSet,
    ReviewViewSet,
    ProductReviewsView
)

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'products/reviews/',
        ProductReviewsView.as_view({'get': 'list'}),
        name='products-reviews'
    ),
]