from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(
        Rental,
        blank=True,
        null=True,
        related_name="rental_info",
        on_delete=models.SET_NULL,
    )
    checkin = models.DateTimeField(null=True)
    checkout = models.DateTimeField(null=True)

    def __str__(self):
        return self.rental.name


