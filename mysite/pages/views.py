from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    # return HttpResponse('<h1>Hello World</h1>')  # string of HTML code
    return render(request, 'home.html', {})


def about_view(request):
    # return HttpResponse('<h1>About Us</h1>')
    context = {
        'data': 'This page is about us',
        'number': '456456',
        'count': [595, 656, 595, 'Abc']
    }
    return render(request, 'about.html', context)
