from rest_framework import serializers
from apps.core.validators import validate_future_date
from .models import Workshop


class WorkshopSerializer(serializers.ModelSerializer):
    spots_left = serializers.SerializerMethodField()

    def get_spots_left(self, obj):
        # если queryset аннотирован bookings_count — берём готовое значение без лишнего запроса
        if hasattr(obj, "bookings_count"):
            return max(0, obj.capacity - obj.bookings_count)
        return max(0, obj.capacity - obj.bookings.count())

    def validate_date(self, value):
        # запрещаем создавать мастер-класс с датой в прошлом
        validate_future_date(value)
        return value

    class Meta:
        model = Workshop
        fields = ["id", "title", "description", "date", "capacity", "spots_left", "image_url", "created_at"]
