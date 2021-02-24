from django.shortcuts import render, redirect
from .models import Account, Transaction
from .forms import TransactionForm, DepositForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime


def entryView(request):
    return render(request, 'account/base.html')


def accountView(request):
    return render(request, 'account/account.html')


@login_required(login_url='login')
def saldoView(request):
    account = Account.objects.filter(owner=request.user.id).first()
    context = {'account': account}
    return render(request, 'account/saldo.html', context)


@login_required(login_url='login')
def transferView(request):
    account = Account.objects.filter(owner=request.user.id).first()
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if account.saldo >= float(request.POST['amount']):
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.owner = request.user
                form_instance.transactionDate = datetime.now()
                form_instance.save()
                amount = form.cleaned_data.get('amount')
                account.pullOutCash(amount)
                account.save()
                messages.success(
                    request, f'Transaction completed: {amount} PLN left.', extra_tags='completed')
                return redirect('saldoView')
            else:
                messages.error(
                    request, f"Transaction canceled: Invalid Input", extra_tags='dataError')
        else:
            messages.error(
                request, f"Transaction canceled: You don't have enaught money", extra_tags='transError')
    else:
        form = TransactionForm()

    context = {
        'account': account,
        'form': form
    }
    return render(request, 'account/transfer.html', context)


@login_required(login_url='login')
def depositView(request):
    account = Account.objects.filter(owner=request.user.id).first()
    form = DepositForm()
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.owner = request.user
            form_instance.destinationAccount = account.accountNumber
            form_instance.transactionDate = datetime.now()
            form_instance.save()
            amount = form.cleaned_data.get('amount')
            account.addCash(amount)
            account.save()
            messages.success(
                request, f'Transaction completed: {amount} PLN added.', extra_tags='added')
            return redirect('saldoView')
    context = {
        'account': account,
        'form': form
    }
    return render(request, 'account/deposit.html', context)


@login_required(login_url='login')
def historyView(request):
    transactions = Transaction.objects.filter(
        owner=request.user).order_by('-transactionDate')
    context = {'transactions': transactions}
    return render(request, 'account/history.html', context)
