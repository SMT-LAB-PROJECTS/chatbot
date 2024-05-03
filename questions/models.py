from django.db import models

# Create your models here.

class Qustion(models.Model):
    question = models.CharField(max_length = 300)
    is_default = models.BooleanField(default = False, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
