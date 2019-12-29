from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import CategoryList

urlpatterns = [
    path('', views.main_list, name='main_list'),
    path('categories', CategoryList.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)