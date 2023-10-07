from rest_framework.permissions import BasePermission


class IsNewUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method == 'POST':
#             return True
#         return request.user == obj
