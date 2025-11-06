from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    def test_todo_creation(self):
        t = Todo.objects.create(title='test')
        self.assertEqual(str(t), 'test')
