from django.shortcuts import render
from . models import Search_detail, search_result
from account.models import User
from django.template.loader import render_to_string
from django.http import JsonResponse,HttpResponse
from django.utils import timezone
from datetime import timedelta
import datetime
from dateutil import parser


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
    context={}
    start_date=''
    end_date=''
    keywords=request.GET.getlist('keyword[]')
    users=request.GET.getlist('user[]')
    time_range=request.GET.getlist('time-range[]')
    
    if 'startdate' in dict(request.GET):
        start_date=request.GET['startdate']
    if 'enddate' in dict(request.GET):
        end_date=request.GET['enddate']


    all_results=search_result.objects.all().prefetch_related('details')
    if len(keywords)>0:
        #without distinct the search result will be displayed for every matched keyword in database
        all_results=all_results.filter(details__keyword__in=keywords).distinct()
    if len(users)>0:
        all_results=all_results.filter(details__user__id__in=users)
    if len(time_range)>0:
        today = timezone.localtime()
        if 'last-month' in time_range:
            all_results=all_results.filter(details__schedule__date__gte=today-timedelta(days=30)).distinct()
        elif 'yesterday' in time_range:
            all_results=all_results.filter(details__schedule__date=today-timedelta(days=1)).distinct()
        elif 'last-week' in time_range:
            all_results=all_results.filter(details__schedule__date__gte=today-timedelta(days=7)).distinct()
    if len(start_date)>0:
        try:
            py_start_date=datetime.datetime.fromtimestamp(int(start_date))
            all_results=all_results.filter(details__schedule__date__gte=py_start_date ).distinct()
        except:
            pass
    if len(end_date)>0:
    
        try:
            py_end_date=datetime.datetime.fromtimestamp(int(end_date))
            all_results=all_results.filter(details__schedule__date__lte=py_end_date ).distinct()
        except:
            pass

    context['results']=all_results
    search_html=render_to_string('searchResults.html',context)
    return JsonResponse({'results':search_html})

        

    

    # if(len(keywords)>0):
        


    # print(keywords)
    # return(request)