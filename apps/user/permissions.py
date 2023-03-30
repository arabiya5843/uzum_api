from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoObjectPermissions


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdminUserOrReadOnly(BasePermission):
    """
    Allows access only to admin users or readonly.
    """

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_superuser)


class IsAdminUserOrMerchantReadOnly(BasePermission):
    """
    Allows access only to admin users or readonly.
    """

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user.type == 'merchant' and request.user.is_superuser)


class IsClientOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            # Allow any user to view product purchases, sellers, and categories
            return True
        # Only allow authenticated buyers to add products to their cart or favorites
        return request.user.is_authenticated and request.user.type == "client"


class IsClient(BasePermission):
    """
    Allows clients to view products, add products to cart and add products to favorites.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.type == 'client')

    def has_object_permission(self, request, view, obj):
        if obj.user.type == 'client' and request.user:
            return True
        return False


class IsMerchant(BasePermission):
    """
    Allows merchants to CRUD products, and add products to wishlist.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.type == 'merchant')


class CustomDjangoObjectPermissions(DjangoObjectPermissions):
    perms_map = {
        # 'GET': ['%(app_label)s.view_%(model_name)s', '%(app_label)s.see_premium_%(model_name)s', ],
        'GET': ['%(app_label)s.see_premium_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsMerchantOrReadOnlyOrAdminUser(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return bool(request.user and request.user.is_superuser)
        else:
            return bool(request.method in SAFE_METHODS or request.user and request.user.type == 'merchant')


class IsMerchantOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.MERCHANT == request.user