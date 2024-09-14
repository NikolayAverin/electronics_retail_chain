from rest_framework.viewsets import ModelViewSet

from retail_chain.models import Contact, Product
from retail_chain.serializers import ContactSerializer, ProductSerializer
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
