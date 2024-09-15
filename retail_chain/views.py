from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from retail_chain.models import Contact, HierarchyElement, Product
from retail_chain.serializers import (ContactSerializer,
                                      HierarchyElementSerializer,
                                      HierarchyElementViewSerializer,
                                      ProductSerializer)
from users.permissions import IsActive


class ContactViewSet(ModelViewSet):
    """Вьюсет для модели контактной информации."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActive,)


class ProductViewSet(ModelViewSet):
    """Вьюсет для модели продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class HierarchyElementViewSet(ModelViewSet):
    """Вьюсет для модели звена иерархии."""

    queryset = HierarchyElement.objects.all()
    serializer_class = HierarchyElementSerializer
    permission_classes = (IsActive,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("country",)

    def get_serializer_class(self):
        """Выбор сериализатора."""
        if self.action in ("list", "retrieve"):
            return HierarchyElementViewSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        """Сохранение страны, города и уровня иерархии."""
        element = serializer.save()
        element.country = element.contact.country
        element.city = element.contact.city
        if element.supplier:
            element.hierarchy_level = element.supplier.hierarchy_level + 1
        else:
            element.hierarchy_level = 0
        element.save()
