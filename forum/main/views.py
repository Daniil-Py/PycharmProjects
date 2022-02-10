from django.shortcuts import render, redirect
from .models import Info
from .forms import InfoForm


def index(request):
    infos = Info.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'infos': infos})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method =='POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная запись'

    form = InfoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

