from django import forms


class CNABFileForm(forms.Form):
    file = forms.FileField()

class TransactionByCPF(forms.Form):
    cpf = forms.CharField(max_length=14)