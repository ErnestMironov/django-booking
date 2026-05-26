from rest_framework import serializers
from .models import Booking
from apps.workshops.serializers import WorkshopSerializer


class BookingSerializer(serializers.ModelSerializer):
    # вложенный объект для чтения; workshop_id принимает id при записи
    workshop = WorkshopSerializer(read_only=True)
    workshop_id = serializers.PrimaryKeyRelatedField(
        source="workshop",
        queryset=__import__("apps.workshops.models", fromlist=["Workshop"]).Workshop.objects.all(),
    )

    class Meta:
        model = Booking
        fields = ["id", "workshop_id", "workshop", "created_at"]
        read_only_fields = ["id", "workshop", "created_at"]
