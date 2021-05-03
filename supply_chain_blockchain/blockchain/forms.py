from django.forms import ModelForm
from django import forms
from .models import Block


class BlockForm(ModelForm):
    class Meta:
        model = Block
        
        fields = ('current_transactions',)
        labels = {'current_transactions': 'Informações sobre a produção do Leite'}


class TransactionForm(forms.Form):
    registro_animal = forms.CharField()
    volume = forms.FloatField()
    dia_horario = forms.DateTimeField()

    tempo_armazenamento = forms.FloatField()
    temperatura_armazenamento = forms.FloatField()
    ph = forms.FloatField()


    registro_veiculo1 = forms.CharField()
    temperatura_transporte = forms.FloatField()
    tempo_transporte = forms.FloatField()

    volume_resfriamento = forms.FloatField()
    dia_hora_resfriamento = forms.DateTimeField()
    temperatura_resfriamento = forms.FloatField()
    ph_resfriamento = forms.FloatField()


    volume_envase = forms.FloatField()
    dia_hora_envase = forms.DateTimeField()
    lote = forms.CharField()

    registro_veiculo_final = forms.CharField()
    temperatura_transporte_final = forms.FloatField()
    tempo_transporte_final = forms.FloatField()




        


        
