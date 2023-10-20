from rest_framework.routers import DefaultRouter
from . import views


app_name = "location"

router = DefaultRouter()
router.register("location", views.LocationViewSet)

urlpatterns = []

urlpatterns += router.urls
