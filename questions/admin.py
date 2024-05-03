from django.contrib import admin
from .models import Qustion

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
  list_display = ("id", "question","is_default", "created_at","updated_at")
  list_display_links = ('question','question')

admin.site.register(Qustion,QuestionAdmin)