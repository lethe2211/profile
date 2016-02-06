from django.shortcuts import render
from django.http.response import HttpResponse

from datetime import date

# Create your views here.
def index(request):
    birthday = 19901122
    t = date.today()
    today = t.year * 10000 + t.month * 100 + t.day
    age = (today - birthday) // 10000
    
    d = {
        'age': age
    }
    return render(request, 'index.html', d)
