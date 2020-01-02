from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Work, Category
from django.db.models import Q

def main_list(request):
    works = Work.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
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

class SearchResultsView(ListView):
    model = Work
    context_object_name = 'results'
    template_name = 'store/search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Work.objects.filter(
            Q(name=query)
        )

        return object_list
