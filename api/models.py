from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Chat(models.Model):
    username = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    @classmethod
    def get_texts(cls, username):
        results = Chat.objects.order_by("created_at").filter(username=username)

        return [{
            'id': result.id,
            'text': result.text
        } for result in results]
