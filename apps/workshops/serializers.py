from rest_framework import serializers
from .models import Workshop


class WorkshopSerializer(serializers.ModelSerializer):
    spots_left = serializers.SerializerMethodField()

    def get_spots_left(self, obj):
        return max(0, obj.capacity - obj.bookings.count())

    class Meta:
        model = Workshop
        fields = ["id", "title", "description", "date", "capacity", "spots_left", "image_url", "created_at"]
