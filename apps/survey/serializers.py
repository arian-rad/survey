from rest_framework import serializers
from .models import Person, Survey, Question, Answer
from rest_framework.exceptions import ValidationError


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

    def validate(self, attrs):
        question = Question.objects.get(id=attrs.get("question"))
        answer = attrs.get("answer")
        if answer < question.from_range or answer > question.to_range:
            raise ValidationError("Invalid answer")
        
        return super().validate(attrs)
