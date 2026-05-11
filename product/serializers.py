from rest_framework import serializers
from .models import Category, Product, Review



class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Название категории должно быть минимум 3 символа"
            )
        return value



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Название товара должно быть минимум 3 символа"
            )
        return value


    def validate_description(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Описание слишком короткое"
            )
        return value


    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Цена должна быть больше 0"
            )
        return value



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


    def validate_text(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Отзыв слишком короткий"
            )
        return value


    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return value