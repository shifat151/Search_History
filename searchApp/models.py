from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from account.models import User

class Search_detail(models.Model):
    keyword=models.CharField(max_length=200)
    schedule=models.DateTimeField(auto_now_add=True, auto_now=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - ({})".format(self.keyword,self.user.username)



class search_result(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    link=models.URLField()
    details=models.ManyToManyField(Search_detail)

    def __str__(self):
        return self.title





