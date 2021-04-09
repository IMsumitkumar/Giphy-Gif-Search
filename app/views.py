from django.shortcuts import render
import urllib
from django.contrib import messages

# from urllib import request
import json
from .forms import SearchForm
from django.http import HttpResponseRedirect

api_key = "cVXPfoOVDz2dPEX6pgejfkJi9do21D8f"

def home(request):
    search_gif_api = "http://api.giphy.com/v1/gifs/search"
    trending_gif_api = "http://api.giphy.com/v1/gifs/trending"

    limit = str(6)

    trending_url = "{url}?&api_key={api_key}&limit={limit}"

    trending_url = trending_url.format(url=trending_gif_api, api_key=api_key, limit=limit)

    with urllib.request.urlopen(trending_url) as response:
        data = json.loads(response.read())

    giphy_urls = []

    for page_no in range(int(limit)):
        url = data.get('data')[page_no].get('embed_url')
        giphy_urls.append(url)


    if request.method == 'POST':
        form = SearchForm(request.POST or None)

        if form.is_valid():
            search_query = form.cleaned_data['search_field']
            search_query = search_query.replace(' ','-')
            instance_limit = str(form.cleaned_data['page_lim_field'])
            
            search_url= "{url}?q={query}&api_key={api_key}&limit={limit}"
            search_url = search_url.format(url=search_gif_api, query=search_query, api_key=api_key, limit=instance_limit)

            with urllib.request.urlopen(search_url) as response:
                data = json.loads(response.read())

            giphy_urls = []
            for page_no in range(int(instance_limit)):
                try:
                    url = data.get('data')[page_no].get('embed_url')
                    giphy_urls.append(url)
                except:
                    giphy_urls = giphy_urls

            if not giphy_urls:
                messages.error(request, "Not Found ... Do not show your foolish creativity here you noob ")
            else:
                context = {'giphy_search_urls':giphy_urls, 'form':form}

                return render(request, 'search.html', context=context)
    else:
        form = SearchForm()

    context = {'giphy_urls':giphy_urls, 'form':form}

    return render(request, 'index.html', context=context)


def trending_sticker(request):

    trending_sticker_api = "https://api.giphy.com/v1/stickers/trending"
    search_sticker_api = "http://api.giphy.com/v1/stickers/search"
    
    limit = str(6)

    trending_sticker_url = "{url}?&api_key={api_key}&limit={limit}"

    trending_sticker_url = trending_sticker_url.format(url=trending_sticker_api, api_key=api_key, limit=limit)

    with urllib.request.urlopen(trending_sticker_url) as response:
        data = json.loads(response.read())

    giphy_urls = []

    for page_no in range(int(limit)):
        url = data.get('data')[page_no].get('embed_url')
        giphy_urls.append(url)
    
    if request.method == 'POST':
        form = SearchForm(request.POST or None)

        if form.is_valid():
            search_query = form.cleaned_data['search_field']
            search_query = search_query.replace(' ','-')
            instance_limit = form.cleaned_data['page_lim_field']
            
            search_url= "{url}?q={query}&api_key={api_key}&limit={limit}"
            search_url = search_url.format(url=search_sticker_api, query=search_query, api_key=api_key, limit=instance_limit)

            with urllib.request.urlopen(search_url) as response:
                data = json.loads(response.read())

            giphy_urls = []
            for page_no in range(int(instance_limit)):
                try:
                    url = data.get('data')[page_no].get('embed_url')
                    giphy_urls.append(url)
                except:
                    giphy_urls = giphy_urls

            if not giphy_urls:
                messages.error(request, "Not Found ...!! Do not show your creativity you idiot ")
            else:

                context = {'giphy_search_urls':giphy_urls, 'form':form}

                return render(request, 'search.html', context=context)
    else:
        form = SearchForm()

    return render(request, 'trending_sticker.html', context={'giphy_urls':giphy_urls, 'form':form})

def upload(request):
    
    context = {}
    return render(request, 'upload_data.html', context=context)