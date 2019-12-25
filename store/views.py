from django.shortcuts import render
from .models import Work
from django.utils import timezone

def work_list(request):
    works = Work.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'store/work_list.html', {'works': works})
