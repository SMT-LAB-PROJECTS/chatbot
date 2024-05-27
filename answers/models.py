from django.db import models
from questions.models import Qustion

# Create your models here.
class Answer(models.Model):
    answer = models.CharField(max_length = 300)
    question_id = models.ForeignKey(Qustion, on_delete=models.CASCADE)
    options = models.ManyToManyField(Qustion, related_name='options', blank = True)
    url = models.URLField(max_length = 200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer
