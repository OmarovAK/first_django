from django.shortcuts import render
from datetime import datetime
from .list_dir import list_dir

def first_page(request):
    my_dict = {
        'title': 'Главная страница'
    }
    return render(request, 'app_first/index.html', my_dict)

def current_time(request):
    time_now = datetime.now()
    time_now = f'{(str(time_now))[11:13]} ч. {(str(time_now))[14:16]}  мин. {(str(time_now))[17:19]} сек.'

    my_dict = {
        'title': 'Страница с текущим временем',
        'time': time_now
    }
    return render(request, 'app_first/current_time.html', my_dict)

def list_files(request):
    my_dict = {
        'title': 'Список документов',
        'list_dir': list_dir,
    }
    return render(request, 'app_first/list_docs.html', my_dict)