from datetime import date
from django.views.generic import ListView
from todo.Models.models import ToDoItem


class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date__gte=date.today())