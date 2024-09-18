from django.urls import path
from .Views.TodayToDos import TodayToDos
from .Views.AllToDos import AllToDos

urlpatterns = [
    path("", AllToDos.as_view(), name="index"),
    path("today/", TodayToDos.as_view(), name="today")
]