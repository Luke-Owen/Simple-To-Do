from django.test import TestCase
from django.urls import reverse
from todo.Tests.Helpers.ToDoHelper import create_todo

class AllToDosViewTest(TestCase):

    def test_today(self):
        todo = create_todo("To be done today", 0)
        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            [todo]
        )

    def test_last_week(self):
        todo = create_todo("This is past due", -7)
        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            []
        )

    def test_next_week(self):
        todo = create_todo("Still have some time", 7)
        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            [todo]
        )