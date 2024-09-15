from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from retail_chain.apps import RetailChainConfig
from retail_chain.views import ContactViewSet, ProductViewSet, HierarchyElementViewSet

app_name = RetailChainConfig.name

contacts_router = SimpleRouter()
contacts_router.register("contacts", ContactViewSet, basename="contacts")
products_router = SimpleRouter()
products_router.register("products", ProductViewSet, basename="products")
hierarchy_element_router = SimpleRouter()
hierarchy_element_router.register("hierarchy-elements", HierarchyElementViewSet, basename="hierarchy-elements")

urlpatterns = [
    path("", include(contacts_router.urls)),
    path("", include(products_router.urls)),
    path("", include(hierarchy_element_router.urls)),
]
