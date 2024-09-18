from datetime import date
from django.views.generic import ListView
from todo.Models.models import ToDoItem

class TodayToDos(ListView):
    model = ToDoItem
    template_name = "todo/today.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())