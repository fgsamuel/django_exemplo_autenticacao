from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(requests):
    return render(requests, 'core/home.html')


@login_required
def pagina1(requests):
    return render(requests, 'core/pagina1.html')


@login_required
def pagina2(requests):
    return render(requests, 'core/pagina2.html')
