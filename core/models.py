
from django.conf import settings
from django.db import models


class Listing(models.Model):
    donor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='listings'
    )

    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    estimated_value = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
