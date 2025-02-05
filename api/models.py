from django.db import models

class User(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    last_name = models.CharField(blank=False, null=False, max_length=200)
    email = models.EmailField(blank=False, null=False, unique=True, max_length=60)
    last_session = models.DateField(blank=True, null=True, default=None)
    created_at = models.DateField(auto_now_add=True, editable=False)
    # One example on how to define a relationship between models
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)

