from django.urls import path
from .views import MyBookingsView, BookingDetailView

urlpatterns = [
    path("my/", MyBookingsView.as_view(), name="my-bookings"),
    path("<int:pk>/", BookingDetailView.as_view(), name="booking-detail"),
]
