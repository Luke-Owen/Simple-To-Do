from datetime import date, timedelta
from todo.Models.models import ToDoItem


def create_todo(todo_text, days):
    return ToDoItem.objects.create(text=todo_text, due_date=date.today() + timedelta(days=days))
