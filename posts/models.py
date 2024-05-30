from django.db import models
from questions.models import Qustion
from answers.models import Answer

# Create your models here.
class Post(models.Model):
    uid = models.CharField(max_length = 200, blank = True)
    message = models.CharField(max_length = 300, blank = True)
    default_response = models.ManyToManyField(Qustion, blank=True, related_name="default_response")
    bot_response = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True, related_name="bot_response")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
