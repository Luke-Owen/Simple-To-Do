from django.test import TestCase
from django.urls import reverse
from todo.Forms.UserInputForm import UserInputForm
from todo.Models.models import ToDoItem


class AddTaskTests(TestCase):
    def setUp(self):
        self.url = reverse('addtask')

    def test_add_task_assert_get_renders_form(self):
        # act
        response = self.client.get(self.url)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/addtask.html')
        self.assertIsInstance(response.context['form'], UserInputForm)

    def test_add_task_assert_post_valid_data(self):
        # arrange
        valid_data = {
            'text': 'Test Task',
            'due_date': '2024-09-18'
        }

        # act
        response = self.client.post(self.url, valid_data)

        # assert
        self.assertEqual(ToDoItem.objects.count(), 1)
        self.assertEqual(ToDoItem.objects.first().text, 'Test Task')
        self.assertRedirects(response, reverse('success'))

    def test_add_task_assert_post_invalid_data(self):
        # arrange
        invalid_data = {
            'text': '',
        }

        # act
        response = self.client.post(self.url, invalid_data)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/addtask.html')
        self.assertIsInstance(response.context['form'], UserInputForm)
        self.assertTrue(response.context['form'].errors)
        self.assertEqual(ToDoItem.objects.count(), 0)





