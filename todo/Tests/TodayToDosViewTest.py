from django.test import TestCase
from django.urls import reverse
from todo.Tests.Helpers.ToDoHelper import create_todo


class TodayToDosViewTest(TestCase):

    def test_today(self):
        todo = create_todo("Today", 0)
        response = self.client.get(reverse("today"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            [todo]
        )

    def test_yesterday(self):
        todo = create_todo("Yesterday", -1)
        response = self.client.get(reverse("today"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            []
        )

    def test_tomorrow(self):
        todo = create_todo("Tomorrow", 1)
        response = self.client.get(reverse("today"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            []
        )