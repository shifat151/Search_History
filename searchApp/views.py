from django.shortcuts import render
from . models import Search_detail, search_result
from account.models import User

from django.db.models import Count
# Create your views here.

def home(request):
    context={}
    keywords=Search_detail.objects.values('keyword').annotate(c=Count('keyword')).order_by('-c')
    users=User.objects.all()
    results=search_result.objects.all().prefetch_related('details')
    context['keywords']=keywords
    context['users']=users
    context['results']=results
    # print(results.__dict__)
    return render(request, 'searchApp/home.html', context)


def filtersResult(request):
    pass
