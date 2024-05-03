from django.contrib import admin
from .models import Answer

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
  list_display = ("id", "answer", "created_at","updated_at")
  list_display_links = ('answer','answer')

admin.site.register(Answer,AnswerAdmin)