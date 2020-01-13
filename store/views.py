from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Work, Category, Style
from django.db.models import Q
from django.utils import timezone

def main_page(request):
    works = Work.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    categories = Category.objects.all()[:5]
    styles = Style.objects.all()

    return render(request, 'store/main_page.html', {
        'works': works,
        'categories': categories,
        'styles': styles
    })

def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'store/work_detail.html', {
        'work': work
    })

def catalog_of_works_in_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    works = Work.objects.filter(category=category)
   
    return render(request, 'store/catalog.html', {
        'works': works,
        'category': category
    })

def catalog_of_works_in_style(request, pk):
    style = get_object_or_404(Style, pk=pk)
    works = Work.objects.filter(style=style)
   
    return render(request, 'store/styles.html', {
        'works': works,
        'style': style
    })


def categories_list(request):
    categories = Category.objects.all()
    
    return render(request, 'store/category_list.html', {
        'categories': categories
    })

def search(request):
    return render(request, 'store/search.html', {})

def search_list(request):
    query = request.GET.get('q')

    filters = Q()

    def reword(a):
        return a[0].upper()+ a[1:len(a)]

    for word in query.split(' '):
        filters |= Q(name__icontains=reword(word))

    works = Work.objects.filter(filters)
    categories = Category.objects.filter(filters)

    return render(request, 'store/search_results.html', {
        'works': works,
        'categories': categories
    })

def contacts(request):
    return render(request, 'store/contacts.html', {})

def about_us(request):
    return render(request, 'store/about_us.html', {})