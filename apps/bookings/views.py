from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError

from .models import Booking
from .serializers import BookingSerializer


class MyBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user).select_related("workshop")
        return Response(BookingSerializer(bookings, many=True).data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        workshop = serializer.validated_data["workshop"]

        booked = workshop.bookings.count()
        if booked >= workshop.capacity:
            return Response({"detail": "Мест нет"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            booking = serializer.save(user=request.user)
        except IntegrityError:
            return Response({"detail": "Вы уже записаны"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)


class BookingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk, user=request.user)
        except Booking.DoesNotExist:
            return Response({"detail": "Не найдено"}, status=status.HTTP_404_NOT_FOUND)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
