from rest_framework import serializers
from .models import Product, Category,Variant,Size,Color,Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['slug']

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

    def create(self, validated_data):
        variant_name = validated_data.get('name')
        if variant_name:
            variant_instance = Variant.objects.filter(name=variant_name).first()
            if variant_instance:
                return variant_instance
            else:
                return super().create(validated_data)
        return super().create(validated_data)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

    def create(self, validated_data):
        size_name = validated_data.get('name')
        if size_name:
            size_instance = Size.objects.filter(name=size_name).first()
            if size_instance:
                return size_instance
            else:
                return super().create(validated_data)
        return super().create(validated_data)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

    def create(self, validated_data):
        color_name = validated_data.get('name')
        color_code = validated_data.get('code')
        if color_name and color_code:

            color_instance = Color.objects.filter(name=color_name, code=color_code).first()
            if color_instance:
                return color_instance
            else:
                return super().create(validated_data)
        return super().create(validated_data)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    variants = VariantSerializer(many=True)
    sizes = SizeSerializer(many=True)
    colors = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        variants_data = validated_data.pop('variants', [])
        sizes_data = validated_data.pop('sizes', [])
        colors_data = validated_data.pop('colors', [])

        category_instance, _ = Category.objects.get_or_create(**category_data)

        product = Product.objects.create(category=category_instance, **validated_data)

        for variant_data in variants_data:
            variant_instance = VariantSerializer().create(variant_data)
            product.variants.add(variant_instance)

        for size_data in sizes_data:
            size_instance = SizeSerializer().create(size_data)
            product.sizes.add(size_instance)

        for color_data in colors_data:
            color_instance = ColorSerializer().create(color_data)
            product.colors.add(color_instance)

        return product

    def update(self, instance, validated_data):
        variants_data = validated_data.pop('variants', [])
        sizes_data = validated_data.pop('sizes', [])
        colors_data = validated_data.pop('colors', [])


        for color_data in colors_data:
            color_name = color_data.get('name')
            color_code = color_data.get('code')
            color, created = Color.objects.get_or_create(name=color_name, code=color_code)
            if color not in instance.colors.all():
                instance.colors.add(color)

        for variant_data in variants_data:
            variant_name = variant_data.get('name')
            variant, created = Variant.objects.get_or_create(name=variant_name)
            if variant not in instance.variants.all():
                instance.variants.add(variant)

        for size_data in sizes_data:
            size_name = size_data.get('name')
            size, created = Size.objects.get_or_create(name=size_name)
            if size not in instance.sizes.all():
                instance.sizess.add(size)



        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image ', instance.image )
        instance.available_stock = validated_data.get('available_stock', instance.available_stock)

        instance.save()

        return instance


class ProductSearchSerializer(serializers.Serializer):
    category = serializers.CharField(required=False)
    min_price = serializers.DecimalField(required=False, decimal_places=2, max_digits=10)
    max_price = serializers.DecimalField(required=False, decimal_places=2, max_digits=10)
    product_name = serializers.CharField(required=False)
    availability = serializers.IntegerField(required=False)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['user']