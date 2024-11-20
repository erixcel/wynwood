from django.shortcuts import render

def index(request):
    options = [
        {'value': '', 'label': 'Selecciona tu destino'},
        {'value': 'paris', 'label': 'París'},
        {'value': 'london', 'label': 'Londres'}
    ]
    return render(request, 'index.html', {'options': options})
