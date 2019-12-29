from django.views.generic import ListView
from .models import Work, Category
from django.shortcuts import render
from django.utils import timezone

def main_list(request):
    works = Work.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categories = Category.objects.all()

    return render(request, 'store/main_list.html', {
        'works': works, 'categories': categories
    })


class CategoryList(ListView):
    queryset = Category.objects.all()
    context_object_name = 'category_list'
    template_name = 'store/category_list.html'