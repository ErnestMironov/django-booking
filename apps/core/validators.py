from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_future_date(value):
    """Workshop date must be in the future."""
    if value <= timezone.now():
        raise ValidationError("Дата должна быть в будущем")
