from django.test import TestCase
from django.urls import reverse
from .models import Chat

class ChatTestCase(TestCase):
    def setUp(self):
        Chat.objects.create(username="test_1", text="text 1")
        Chat.objects.create(username="test_1", text="text 2")
        Chat.objects.create(username="test_2", text="text 3")

    # Model Tests
    def test_chats_exist(self):
        self.assertEqual(Chat.objects.count(), 3)

    def test_get_texts_returns_values(self):
        user_1 = Chat.objects.filter(username="test_1").first()
        expected = [
            {'id': user_1.id, 'text': user_1.text},
            {'id': user_1.id, 'text': user_1.text}
        ]

        self.assertEqual(Chat.get_texts(user_1.username), expected)
