from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Chat
from .forms import ChatForm

@csrf_exempt
def chat(request):
    if request.method == "POST" and request.GET['username'] and request.GET['text']:
        new_chat = Chat.objects.create(
            username=request.GET['username'],
            text=request.GET['text'],
            updated_at = timezone.now()
        )
        response = {'id': new_chat.id}
    elif request.method == "GET" and request.GET['username']:
        response = Chat.get_texts(request.GET['username'])
    else:
        return 404

    return JsonResponse(response, safe=False)
