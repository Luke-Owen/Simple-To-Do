from django.shortcuts import render
from django.urls import path
from .Views.TodayToDos import TodayToDos
from .Views.AllToDos import AllToDos
from .Views.AddTask import add_task

urlpatterns = [
    path("", AllToDos.as_view(), name="index"),
    path("today/", TodayToDos.as_view(), name="today"),
    path("addtask/", add_task, name="addtask"),
    path('success/', lambda request: render(request, 'todo/success.html'), name='success'),
]