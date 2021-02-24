from django.urls import path
from . import views

urlpatterns = [
    path('', views.entryView, name='entryView'),
    path('account/', views.accountView, name='accountView'),
    path('account/saldo/', views.saldoView, name='saldoView'),
    path('account/transfer/', views.transferView, name='transferView'),
    path('account/deposit/', views.depositView, name='depositView'),
    path('account/history/', views.historyView, name='historyView'),
    path('account/import/', views.importHistory, name='importHistory'),
]
