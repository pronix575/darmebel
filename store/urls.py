from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

handler404 = 'store.views.e404'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('work/<int:pk>/', views.work_detail, name="work_detail"),
    path('catalog/category/<int:pk>/', views.catalog_of_works_in_category, name="catalog_of_works_in_category"),
    path('catalog/style/<int:pk>/', views.catalog_of_works_in_style, name="catalog_of_works_in_style"),
    path('catalog/', views.categories_list, name="categories_list"),
    path('search/', views.search, name="search"),
    path('search results/', views.search_list, name="search results"),
    path('contacts/', views.contacts, name="contacts"),
    path('about us/', views.about_us, name="about_us"),
    path('request/', views.request, name="request"),
    path('request done/', views.request_done, name="request_done"),
    path('request list/', views.request_list, name="request_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)