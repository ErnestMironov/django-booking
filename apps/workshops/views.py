from rest_framework import viewsets, permissions
from apps.users.permissions import IsAdminRole
from .models import Workshop
from .serializers import WorkshopSerializer


class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all().order_by("date")
    serializer_class = WorkshopSerializer

    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [permissions.AllowAny()]
        return [IsAdminRole()]
