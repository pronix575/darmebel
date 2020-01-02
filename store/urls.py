from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import CategoryList

urlpatterns = [
    path('', views.main_list, name='main_list'),
    path('work/<int:pk>/', views.work_detail, name="work_detail"),
    path('catalog/<int:pk>/', views.catalogOfWorksInCategory, name="catalogOfWorksInCategory"),
    path('categories', CategoryList.as_view()),
    path('search', views.search, name="search"),
    path('search results', views.search_list, name="search results"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
