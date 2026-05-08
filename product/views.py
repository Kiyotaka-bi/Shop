from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Avg, Count

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.annotate(products_count=Count('product'))
    serializer_class = CategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class ProductReviewsView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        data = []

        for product in products:
            reviews = product.reviews.all()
            avg_rating = reviews.aggregate(avg=Avg('stars'))['avg']

            data.append({
                "id": product.id,
                "title": product.title,
                "reviews": [
                    {
                        "text": r.text,
                        "stars": r.stars
                    } for r in reviews
                ],
                "rating": avg_rating if avg_rating else 0
            })

        return Response(data)