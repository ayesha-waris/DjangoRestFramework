from cgitb import lookup
from requests import request
from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPErmissionMixin():
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission]


class UserQuertSetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        user = self.request.user
        # if user.is_staff:
        #   return qs
        return qs.filter(**lookup_data)
