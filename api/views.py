from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Chat
from .forms import ChatForm

def chat(request):
    if request.method == "POST":
        obj, created = Chat.objects.get_or_create(username=request.POST['username'])
        if obj:
            obj.text = request.POST['text']
            obj.updated_at = timezone.now()
            obj.save()
    else:
        obj = Chat.get_texts(request.GET['username'])

    return JsonResponse(obj, safe=False)
