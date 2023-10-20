from django.db import models
from django.utils.translation import gettext as _


class LocationTypeChoices(models.TextChoices):
    COUNTRY = "country", _("country")
    CITY = "city", _("city")


class Location(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50, unique=True)
    type = models.CharField(verbose_name=_("Type"), max_length=7, choices=LocationTypeChoices.choices)
    country = models.ForeignKey("self", verbose_name=_("Country"), null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
