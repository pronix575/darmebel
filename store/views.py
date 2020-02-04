from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Work, Category, Style, Request, MainPagePreview, Contact
from django.db.models import Q
from django.utils import timezone

def main_page(request):
    works = Work.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    categories = Category.objects.all()[:5]
    styles = Style.objects.all()
    preview = MainPagePreview.objects.last()
    contacts = Contact.objects.last()

    return render(request, 'store/main_page.html', {
        'works': works,
        'categories': categories,
        'styles': styles,
        'preview': preview,
        'contacts': contacts
    })

def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)

    if not request.user.is_authenticated:
        work.views += 1

        work.save()

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

    if query == "" or query[0] == " " or query[len(query) - 1] == " ":
        return render(request, 'store/nothing_in_results.html', {})
    else:      

        filters = Q()

        def reword(a):
            
            return a[0].upper()+ a[1:len(a)]

        for word in query.split(' '):
            filters |= Q(name__icontains=reword(word))

            works = Work.objects.filter(filters)
            categories = Category.objects.filter(filters)
            styles = Style.objects.filter(filters)


        if works or categories or styles:
            return render(request, 'store/search_results.html', {
                'works': works,
                'categories': categories,
                'styles': styles
            })
        else:    
            if len(query) > 20:
                query = query[0:20] + '...'

            query = 'по запросу "' + query + '"'    

            return render(request, 'store/nothing_in_results.html', {'query': query})

def request(request):
    if request.method == "POST":    
        name = request.POST.get('q_name')
        phone_number = request.POST.get('q_phone')
        email = request.POST.get('q_email')
        category_id = request.POST.get('select')
        
        if category_id == '':
            Request.objects.create(name=name[0:50], phone=phone_number, email=email, category_id=0)
        else:
            Request.objects.create(name=name[0:50], phone=phone_number, email=email, category_id=category_id)    
                    

        requests = Request.objects.all()

        return redirect('/request done')
    else:
        return redirect('/e404')      

def delete_request(request):
    id_n = request.POST.get('id')

    req = Request.objects.get(id=id_n)
    req.is_alive = False
    req.save()

    return redirect('/request list')


def request_done(request):
    return render(request, 'store/request_done.html')


def request_list(request):
    if request.user.is_authenticated:        
        requests = Request.objects.filter(is_alive=True)

        return render(request, 'store/request_list.html', {
            "requests": requests
        })
    else:
        return render(request, 'store/err404.html', {})  

def request_detail(request, pk):
    if request.user.is_authenticated:    
        request221 = get_object_or_404(Request, pk=pk)
            
        if request221.is_alive:    
            if not request221.is_viewed:    
                request221.is_viewed = True
                request221.save()

                if  request221.category_id != 0:
                    category = Category.get_object_or_404(request221, pk=request221.category_id)
                else:
                    category = False

            return render(request, 'store/request_detail.html', {
                "request": request221,
                "category": category
            })
        else:
            return redirect('/e404')    

    else:
        return render(request, 'store/err404.html', {})  

def contacts(request):
    contacts = Contact.objects.last()

    return render(request, 'store/contacts.html', {
        'contacts': contacts
    })

def about_us(request):
    return render(request, 'store/about_us.html', {})

def e404f(request):
    return render(request, 'store/err404.html', {})

def e404(request, exeption):
    return render(request, 'store/err404.html', {})

