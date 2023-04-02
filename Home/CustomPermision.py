from rest_framework import permissions
from .models import Course
from manager.models import DoneVideos


class PaymentVerified(permissions.BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.subscriptiontype != "N")
    
class isAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or  request.user.is_staff)
          
class isOwnorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.method in permissions.SAFE_METHODS or obj.user == request.user)
    

class Authorized_toGive_Review(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        doneVedeosByStudent = DoneVideos.objects.filter(student = request.user)
        result = False
        for vide in doneVedeosByStudent:
            if (vide.course == obj):
                result = True

        return result