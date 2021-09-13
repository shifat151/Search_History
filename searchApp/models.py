from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from account.models import User

class Search_details(models.Model):
    keyword=models.CharField(max_length=200)
    schedule=models.DateTimeField(auto_now_add=True, auto_now=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


class search_results(models.Model):
    descripton=models.CharField(max_length=200)
    link=models.URLField()
    details=models.ManyToManyField(Search_details)




