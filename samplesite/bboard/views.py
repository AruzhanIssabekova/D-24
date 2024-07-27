from django.core.paginator import Paginator
import requests
from django.shortcuts import render

def fetch_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json()

def post_list(request):
    data = fetch_data()

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'bboard/post_list.html', context)
