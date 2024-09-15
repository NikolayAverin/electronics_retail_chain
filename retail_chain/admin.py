from django.contrib import admin

from retail_chain.models import Contact, HierarchyElement, Product


@admin.action(description="Очистить задолженность")
def set_debt_to_zero(modeladmin, request, queryset):
    """Очистка задолженности."""
    queryset.update(debt=0)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Просмотр контактной информации."""

    list_display = ("id", "email", "country", "city", "street", "house_number")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Просмотр продуктов."""

    list_display = ("id", "title", "product_model", "release_date")


@admin.register(HierarchyElement)
class HierarchyElementAdmin(admin.ModelAdmin):
    """Просмотр звеньев иерархии."""

    list_display = (
        "id",
        "name",
        "country",
        "city",
        "contact",
        "product",
        "supplier",
        "debt",
        "created_at",
        "hierarchy_type",
        "hierarchy_level",
    )
    list_display_links = ("supplier",)
    list_filter = ("city",)
    actions = [set_debt_to_zero]
