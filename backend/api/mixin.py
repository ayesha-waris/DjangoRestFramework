from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPErmissionMixin():
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission]