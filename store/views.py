from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Work, Category, PreviewWork
from django.db.models import Q

def main_list(request):
    works = PreviewWork.objects.all()
    categories = Category.objects.all()

    return render(request, 'store/main_list.html', {
        'works': works,
        'categories': categories
    })

def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'store/work_detail.html', {
        'work': work
    })

def catalogOfWorksInCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    works = Work.objects.filter(category=category)
    return render(request, 'store/catalog.html', {
        'works': works,
        'category': category
    })

class CategoryList(ListView):
    queryset = Category.objects.all()
    context_object_name = 'category_list'
    template_name = 'store/category_list.html'

def search(request):
    return render(request, 'store/search.html', {})

def search_list(request):
    query = request.GET.get('q')

    works = Work.objects.filter(Q(name=query))
    categories = Category.objects.filter(Q(name=query))

    return render(request, 'store/search_results.html', {
        'works': works,
        'categories': categories
    })

def contacts(request):
    return render(request, 'store/contacts.html', {})

def about_us(request):
    return render(request, 'store/about_us.html', {})