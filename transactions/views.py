from django.utils import translation
from django.shortcuts import render, get_object_or_404
from .models import Transaction
from .serializers import TransactionSerializer
from datetime import datetime

def data_extractor(file):
    transactions = []
    content = file.read().decode("utf-8")
    for line in content.split("\n"):
        transactions.append({
            'type': line[0],
            'date': datetime.strptime(line[1:9], '%Y%m%d').date(),
            'value': round(float(line[9:19]), 2) / 100,
            'cpf': line[19:30],
            'card': line[30:42],
            'time': datetime.strptime(line[42:48], '%H%M%S').time(),
            'owner': line[48:62].strip(),
            'store': line[62:81].strip()
        })

    return transactions


def create_transaction(request):
    try:
        if request.method == 'POST':
            file = request.FILES.get('file')
            if file:
                transactions = data_extractor(file)
                context = {'transactions': transactions}

                for transaction in transactions:
                    serializer = TransactionSerializer(data=transaction)
                    if serializer.is_valid():
                        serializer.save()
                    
                return render(request, 'transactions.html', context)
        return render(request, 'home.html')
    except Exception as e:

        context = {'error': e, 'language_code': translation.get_language()}
        return render(request, '404.html', context)


def list_transactions(request):
    transactions = Transaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'transactions.html', context)


def transactions_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    context = {'transaction': transaction}
    return render(request, 'transaction_detail.html', context)


def handle_404(request, exception):
    return render(request, '404.html', status=404)

def search_cpf(request):
    if request.method == 'GET':
        cpf = request.GET.get('cpf')
        cpf = ''.join(filter(str.isdigit, cpf))
        transactions = Transaction.objects.filter(cpf__contains=cpf)
        context = {'transactions': transactions}
        return render(request, 'transactions.html', context)
