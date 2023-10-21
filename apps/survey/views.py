from rest_framework import viewsets
from .serializers import (
    PersonSerializer,
    SurveySerializer,
    QuestionSerializer,
    AnswerSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Person, Survey, Question, Answer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

    @action(methods=["GET"], url_path="survey-questions", detail=True)
    def get_questions(self, request, pk):
        questions = Question.objects.filter(survey=pk)
        return Response(QuestionSerializer(questions, many=True).data)


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
