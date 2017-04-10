from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Chat
from .forms import ChatForm

@csrf_exempt
def chat(request):
    if request.method == "POST":
        obj, created = Chat.objects.get_or_create(username=request.POST['username'])
        if obj:
            obj.text = request.POST['text']
            obj.updated_at = timezone.now()
            obj.save()
    elif request.method == "GET" and request.GET['username']:
        obj = Chat.get_texts(request.GET['username'])
    else:
        return 404

    return JsonResponse(obj, safe=False)
