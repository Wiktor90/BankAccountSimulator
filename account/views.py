from django.shortcuts import render, redirect


def entryView(request):
    return render(request, 'account/base.html')


def accountView(request):
    return render(request, 'account/account.html')


def saldoView(request):
    return render(request, 'account/saldo.html')


def transferView(request):
    return render(request, 'account/transfer.html')


def depositView(request):
    return render(request, 'account/deposit.html')


def historyView(request):
    return render(request, 'account/history.html')
