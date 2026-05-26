from django.db import models
from apps.core.validators import validate_future_date


class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(validators=[validate_future_date])
    capacity = models.PositiveIntegerField()
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
