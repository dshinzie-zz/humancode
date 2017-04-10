from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Chat
from .forms import ChatForm

def get_post_response(post_params):
    if post_params['username'] and post_params['text'] and post_params['timeout']:
        new_chat = Chat.objects.create(
            username=post_params['username'],
            text=post_params['text'],
            updated_at = timezone.now()
        )

        return {'id': new_chat.id}
    elif post_params['username'] and post_params['text']:
        new_chat = Chat.objects.create(
            username=post_params['username'],
            text=post_params['text'],
            updated_at = timezone.now()
        )
        return {'id': new_chat.id}
    else:
        return HttpResponseBadRequest()

@csrf_exempt
def chat(request):
    if request.method == "POST":
        response = get_post_response(request.GET)
    elif request.method == "GET" and request.GET['username']:
        response = Chat.get_texts(request.GET['username'])
    else:
        return HttpResponseBadRequest()

    return JsonResponse(response, safe=False)
