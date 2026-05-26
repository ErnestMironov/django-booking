from django.db.models import Count
from rest_framework import viewsets, permissions
from apps.users.permissions import IsAdminRole
from .models import Workshop
from .serializers import WorkshopSerializer


class WorkshopViewSet(viewsets.ModelViewSet):
    serializer_class = WorkshopSerializer

    def get_queryset(self):
        # считаем бронирования одним запросом, чтобы не было N+1 в spots_left
        return Workshop.objects.annotate(bookings_count=Count("bookings")).order_by("date")

    # чтение открыто всем, изменение — только администратору
    def get_permissions(self):
        if self.action in ("list", "retrieve"):
            return [permissions.AllowAny()]
        return [IsAdminRole()]
