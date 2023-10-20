from django.contrib import admin
from .models import Location, LocationTypeChoices
from django.core.validators import EMPTY_VALUES
from django import forms


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

    def clean(self):
        location_type = self.cleaned_data.get("type")

        if (
            location_type == LocationTypeChoices.CITY
            and self.cleaned_data.get("country") in EMPTY_VALUES
        ):
            self._errors["country"] = self.error_class(["Country must be defined"])
        return self.cleaned_data


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    form = LocationForm
