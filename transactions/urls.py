from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_transaction, name='home'),
    path('transactions/', views.list_transactions, name='transactions'),
    path('transaction/<int:pk>/', views.transactions_detail, name='transaction_detail'),
    path('search/', views.search_cpf, name='search'),
]
