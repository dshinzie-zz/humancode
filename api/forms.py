from django import forms
from .models import Chat

class RoomForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('username', 'text')
