from rest_framework import viewsets, permissions
from .models import Workshop
from .serializers import WorkshopSerializer


class WorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workshop.objects.all().order_by("date")
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.AllowAny]
