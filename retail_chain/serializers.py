from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from retail_chain.models import Contact, Product, HierarchyElement
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
    # country = SerializerMethodField()
    #
    # def get_country(self, obj):
    #     return obj.contact.country

    class Meta:
        model = HierarchyElement
        fields = ("name", "contact", "product", "supplier", "hierarchy_type", "country")
        validators = [SupplierValidator(supplier="supplier", hierarchy_type="hierarchy_type"),]


class HierarchyElementViewSerializer(ModelSerializer):
    """Сериализатор звена иерархии для просмотра."""
    # country = SerializerMethodField()
    # # hierarchy_level = SerializerMethodField()
    #
    # def get_country(self, obj):
    #     return obj.contact.country
    #
    # # def get_hierarchy_level(self, obj):
    # #     if obj.supplier:
    # #         obj.hierarchy_level = obj.supplier.hierarchy_level + 1
    # #     else:
    # #         obj.hierarchy_level = 1
    # #     return obj.hierarchy_level

    class Meta:
        model = HierarchyElement
        fields = "__all__"
