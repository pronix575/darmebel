from django.contrib import admin
from .models import Category, Work, Style, Request, MainPagePreview

class ExampleAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(MainPagePreview, ExampleAdmin)
admin.site.register(Category)
admin.site.register(Work)
admin.site.register(Style)

