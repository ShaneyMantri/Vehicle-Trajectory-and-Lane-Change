from django import forms
from .models import image_received

class ImageReceivedForm(forms.ModelForm):
    class Meta:
        model=image_received
        fields = ('image',)