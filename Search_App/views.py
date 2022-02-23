from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from Search_App.forms import SearchForm
from Search_App.models import SearchHis
from django.db.models import Count
from django.contrib.auth.models import User
import requests
from bs4 import BeautifulSoup as bs
from django.db.models import Q
from itertools import chain

import lxml


# Create your views here.
def home(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            search = form.save(commit=False)
            if request.user == True:
                search.searcher = request.user
                search.save()
            else:
                pass
            keyword = form.cleaned_data.get('keyword')
            url = 'https://www.ask.com/web?q=' + keyword
            res = requests.get(url)
            soup = bs(res.text, 'lxml')
            result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

            final_result = []

            for result in result_listings:
                result_title = result.find(class_='PartialSearchResults-item-title').text
                result_url = result.find('a').get('href')
                result_desc = result.find(class_='PartialSearchResults-item-abstract').text

                final_result.append((result_title, result_url, result_desc))

            return render(request, 'Search_App/home.html', context={'form': form, 'final_result': final_result})
    else:

        return render(request, 'Search_App/home.html', context={'form': form})


def history(request):
    keyword = SearchHis.objects.values('keyword').annotate(total=Count('keyword'))
    user = User.objects.all()

    context = {

        'keyword': keyword,
        'user': user,
    }
    return render(request, 'Search_App/history.html', context)


def search(request):
    keyword = SearchHis.objects.values('keyword').annotate(total=Count('keyword'))
    user = User.objects.all()
    query = request.POST.get('search', '')
    if query:
        queryset = (Q(keyword__icontains=query)) | (Q(date__icontains=query)) | (
            Q(searcher__username__icontains=query)) | (Q(searcher__email__icontains=query))
        results = SearchHis.objects.filter(queryset).distinct()
    else:
        results = []
    return render(request, 'Search_App/history.html', context={'results': results, 'keyword': keyword, 'user': user, })


def filter(request):
    keyword = SearchHis.objects.values('keyword').annotate(total=Count('keyword'))
    user = User.objects.all()
    users = request.POST.get('user', '')
    keywords = request.POST.get('keyword', '')
    fromdate = request.POST.get('fromdate', '')
    todate = request.POST.get('todate', '')
    if users or keywords:
        queryset = (Q(keyword__icontains=keywords)) & (Q(searcher__username__icontains=users))
        results = SearchHis.objects.filter(queryset).distinct()
        if fromdate:
            results = results.filter(date__gte=fromdate)
        if todate:
            results = results.filter(date__lte=todate)
        else:
            results = []
    else:
        results = []
    return render(request, 'Search_App/history.html', context={'results': results, 'keyword': keyword, 'user': user, })
