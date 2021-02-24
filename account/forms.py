from .models import Transaction
from django import forms
from django.forms import ModelForm


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        exclude = ['owner', 'transactionDate']


class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['owner', 'destinationAccount', 'transactionDate']
