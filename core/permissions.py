from rest_framework import permissions

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return (super().has_permission(request, view) or
                request.method == 'POST')


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwnerOrAdmin(IsOwner):
    def has_object_permission(self, request, view, obj):
        return (super().has_object_permission(request, view, obj) or
                view.action == 'retrieve' and request.user.is_superuser)
