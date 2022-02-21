from django.db import models
from django.contrib.auth.models import User

class SearchHis(models.Model):
    searcher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='searcher')
    keyword = models.CharField(max_length=264, blank=True)
    date = models.DateTimeField(auto_now_add=True)

