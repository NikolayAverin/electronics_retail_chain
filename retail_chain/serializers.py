from rest_framework.serializers import ModelSerializer

from retail_chain.models import Contact, Product


class ContactSerializer(ModelSerializer):
    """Сериализатор контактной информации."""

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    """Сериализатор продукта."""

    class Meta:
        model = Product
        fields = "__all__"
