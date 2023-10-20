from rest_framework.routers import DefaultRouter
from . import views


app_name = "survey"

router = DefaultRouter()
router.register("person", views.PersonViewSet)
router.register("survey", views.SurveyViewSet)
router.register("question", views.QuestionViewSet)
router.register("answer", views.AnswerViewSet)

urlpatterns = []

urlpatterns += router.urls
