from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Chat
from .forms import ChatForm
import time

def create_chat(post_params):
    if 'timeout' in post_params:
        timeout = float(post_params['timeout'])
    else:
        timeout = float(60)

    return Chat.objects.create(
        username = post_params['username'],
        text = post_params['text'],
        expiration_time = time.time() + timeout,
        updated_at = timezone.now()
    )

def get_post_response(post_params):
    if post_params['username'] and post_params['text']:
        new_chat = create_chat(post_params)

        return {'id': new_chat.id}
    else:
        return HttpResponseBadRequest()

def get_request_variables(input_request):
    if 'username' in input_request.POST:
        return input_request.POST
    else:
        return input_request.GET

@csrf_exempt
def chat(request):
    if request.method == "POST":
        request_variables = get_request_variables(request)
        response = get_post_response(request_variables)
    elif request.method == "GET" and request.GET['username']:
        response = Chat.get_texts(request.GET['username'])
    else:
        return HttpResponseBadRequest()

    return JsonResponse(response, safe=False)
