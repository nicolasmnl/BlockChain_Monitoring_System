from django.forms import ModelForm
from .models import Block


class BlockForm(ModelForm):
    class Meta:
        model = Block
        fields = ('current_transactions',)
        labels = {'current_transactions': 'Informações sobre a produção do Leite'}
