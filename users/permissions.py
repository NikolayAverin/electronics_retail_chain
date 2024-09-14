from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """Проверка активности пользователя."""

    def has_object_permission(self, request, view, obj):
        return obj.is_active
