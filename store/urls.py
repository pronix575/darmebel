from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('work/<int:pk>/', views.work_detail, name="work_detail"),
    path('catalog/<int:pk>/', views.catalogOfWorksInCategory, name="catalogOfWorksInCategory"),
    path('categories', views.categories_list, name="categories_list"),
    path('search', views.search, name="search"),
    path('search results', views.search_list, name="search results"),
    path('contacts', views.contacts, name="contacts"),
    path('about us', views.about_us, name="about_us")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
