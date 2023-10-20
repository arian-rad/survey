from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from apps.location.models import Location


class Person(models.Model):
    first_name = models.CharField(verbose_name=_("First name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=50)
    city = models.ForeignKey(Location, verbose_name=_("City"), on_delete=models.CASCADE)
    email = models.EmailField(verbose_name=_("Email"))

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name


class Survey(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=50)
    description = models.TextField(verbose_name=_("Description"), max_length=1000)
    creator = models.ForeignKey(
        User, verbose_name=_("Creator"), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(verbose_name=_("Text"), max_length=1000)
    from_range = models.PositiveSmallIntegerField(verbose_name=_("From range"))
    to_range = models.PositiveSmallIntegerField(verbose_name=_("To range"))
    survey = models.ForeignKey(
        Survey, verbose_name=_("Survey"), on_delete=models.CASCADE
    )
    # can add priority

    def __str__(self):
        return self.text[:15]


class Answer(models.Model):
    answer = models.PositiveSmallIntegerField(verbose_name=_("Answer"))
    question = models.ForeignKey(
        Question, verbose_name=_("Question"), on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person, verbose_name=_("person"), on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.answer}, {self.question}"
