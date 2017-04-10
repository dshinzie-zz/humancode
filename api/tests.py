from django.test import TestCase
from django.urls import reverse
from .models import Chat
from django.test import Client
import time

class ChatTestCase(TestCase):
    def setUp(self):
        Chat.objects.create(username="test_1", text="text 1", expiration_time=time.time() + 5000)
        Chat.objects.create(username="test_1", text="text 2", expiration_time=time.time() + 5000)
        Chat.objects.create(username="test_2", text="text 3", expiration_time=time.time() + 5000)

    def test_chats_exist(self):
        self.assertEqual(Chat.objects.count(), 3)

    def test_get_texts_returns_values(self):
        chat_1 = Chat.objects.filter(username="test_1").first()
        chat_2 = Chat.objects.filter(username="test_1").last()
        expected = [
            {'id': chat_1.id, 'text': chat_1.text},
            {'id': chat_2.id, 'text': chat_2.text}
        ]

        self.assertEqual(Chat.get_texts(chat_1.username), expected)

    def test_only_returns_unexpired_texts(self):
        Chat.objects.create(username="expired_test", text="text 1", expiration_time=time.time() + 5000)
        Chat.objects.create(username="expired_test", text="text 2", expiration_time=time.time())
        chat_1 = Chat.objects.filter(username="expired_test").first()
        chat_2 = Chat.objects.filter(username="expired_test").last()
        expected = [{'id': chat_1.id, 'text': chat_1.text}]

        self.assertEqual(Chat.get_texts(chat_1.username), expected)

    def test_get_requests_are_successful_for_valid_params(self):
         client = Client()
         response = client.get('/chat', {'username': 'test_1'})

         self.assertEqual(response.status_code, 200)

    def test_post_request_are_successful(self):
         client = Client()
         response = client.post('/chat', {'username': 'test_2', 'text': 'test'})

         self.assertEqual(response.status_code, 200)
