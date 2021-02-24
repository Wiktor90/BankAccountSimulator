from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxLengthValidator, RegexValidator
from datetime import datetime
import random


class Account(models.Model):

    def accountGenerator():
        seq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        account = [random.choice(seq) for i in range(0, 12)]
        account = "".join(account)
        return account

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(decimal_places=2, max_digits=10, validators=[
                                MinValueValidator(0.00)])
    accountNumber = models.CharField(
        max_length=12, unique=True, default=accountGenerator)
    created_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.owner} - {self.accountNumber}'

    def pullOutCash(self, amount):
        self.saldo = self.saldo - amount
        return self.saldo

    def addCash(self, amount):
        self.saldo = self.saldo + amount
        return self.saldo


class Transaction(models.Model):
    numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    destinationAccount = models.CharField(max_length=12, validators=[numeric])
    amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[
        MinValueValidator(0.01)])
    transactionDate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.owner} - {self.title} - {self.transactionDate}'
