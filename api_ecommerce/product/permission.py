from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):


    def has_permission(self, request, view):
        # Allow read-only permissions for non-admin users (GET requests)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is an admin to allow creation (POST requests)
        return request.user and request.user.is_staff
