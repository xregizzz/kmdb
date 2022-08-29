from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Review


class IsReviewOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, review: Review):

        if request.user == review.user:
            return True

        return request.user.is_superuser
