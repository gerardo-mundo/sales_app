from typing import Required
from django.db import models

class User(models.Model):
    name = models.CharField(Required, max_length=200)
    last_name = models.CharField(Required, max_length=200)
    email = models.EmailField(Required, max_length=60)
    last_session = models.DateField(null=True)
    created_at = models.DateField(auto_created=True, editable=False)
    # One example on how to define a relationship between models
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)

