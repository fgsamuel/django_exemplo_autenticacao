from django.shortcuts import render


def home(requests):
    return render(requests, 'core/home.html')


def pagina1(requests):
    return render(requests, 'core/pagina1.html')


def pagina2(requests):
    return render(requests, 'core/pagina2.html')
