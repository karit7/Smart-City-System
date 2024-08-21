from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):

        # Any permissions only allowed to superUser
        return request.user.is_superuser

class IsSuperUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the superUser
        print('request.user.is_superuser = ', request.user.is_superuser)
        return request.user.is_superuser
