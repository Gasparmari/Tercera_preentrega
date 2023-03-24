from django import forms

class BandasForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    mejor_disco = forms.CharField(max_length=20)
    anio = forms.IntegerField()

class BuscarbandaForm(forms.Form):
    banda = forms.CharField(max_length=20)
