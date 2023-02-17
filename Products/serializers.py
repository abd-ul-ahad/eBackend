from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    product_id = serializers.ReadOnlyField()
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = "__all__"

    # As shown in this function we will add get_ before the name of functions in this class fields
    # Example the function was my_discount and here it is get__discount

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
