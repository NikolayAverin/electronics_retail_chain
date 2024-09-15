from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from retail_chain.models import Contact, HierarchyElement, Product
from retail_chain.validators import SupplierValidator


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


class HierarchyElementSerializer(ModelSerializer):
    """Сериализатор звена иерархии."""

    class Meta:
        model = HierarchyElement
        fields = ("name", "contact", "product", "supplier", "hierarchy_type", "country")
        validators = [
            SupplierValidator(supplier="supplier", hierarchy_type="hierarchy_type"),
        ]


class HierarchyElementViewSerializer(ModelSerializer):
    """Сериализатор звена иерархии для просмотра."""

    class Meta:
        model = HierarchyElement
        fields = "__all__"
