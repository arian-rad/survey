from rest_framework import viewsets
from .serializers import (
    PersonSerializer,
    SurveySerializer,
    QuestionSerializer,
    AnswerSerializer,
)
from .models import Person, Survey, Question, Answer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
