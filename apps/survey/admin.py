from django.contrib import admin
from .models import Person, Survey, Question, Answer


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


class QuestionInline(admin.StackedInline):
    model = Question


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("title", "creator")
    inlines = (QuestionInline,)
    readonly_fields = ("creator",)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "from_range", "to_range")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer", "question", "person")

