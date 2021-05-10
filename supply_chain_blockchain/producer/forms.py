from django.forms import ModelForm
from django import forms
from .models import Producer

class ProductProducerForm(ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'