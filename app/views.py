from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import *
def home(request):
    # Получение списка объектов из модели
    queryset = News.objects.all()

    # Количество элементов на одной странице
    items_per_page = 24

    # Создание объекта Paginator
    paginator = Paginator(queryset, items_per_page)

    # Получение номера текущей страницы из параметров запроса
    page = request.GET.get('page')

    try:
        # Получение объекта текущей страницы
        items = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не является целым числом, вывод первой страницы
        items = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального, вывод последней страницы
        items = paginator.page(paginator.num_pages)
    return render(request,"app/base.html",{'items': items})
def announcement(request):
    # Получение списка объектов из модели
    queryset = Ad.objects.all()

    # Количество элементов на одной странице
    items_per_page = 24

    # Создание объекта Paginator
    paginator = Paginator(queryset, items_per_page)

    # Получение номера текущей страницы из параметров запроса
    page = request.GET.get('page')

    try:
        # Получение объекта текущей страницы
        items = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не является целым числом, вывод первой страницы
        items = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального, вывод последней страницы
        items = paginator.page(paginator.num_pages)
    return render(request, "app/Announcement.html", {'items': items})
def journal(request):
    # Получение списка объектов из модели
    queryset = Journal.objects.all()
    # Количество элементов на одной странице
    items_per_page = 24

    # Создание объекта Paginator
    paginator = Paginator(queryset, items_per_page)

    # Получение номера текущей страницы из параметров запроса
    page = request.GET.get('page')

    try:
        # Получение объекта текущей страницы
        items = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр page не является целым числом, вывод первой страницы
        items = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального, вывод последней страницы
        items = paginator.page(paginator.num_pages)
    return render(request, "app/Journal.html", {'items': items})

def Journal_View(request,pk):
    print(pk)
    return render(request, "app/Journal_view.html", {'items': News.objects.filter(journal=pk)})
class Announcement_DT(DetailView):
    model=Ad
    template_name = "app/announcement_dt.html"

class Arcticle(DetailView):
    model = News
    template_name = "app/article.html"