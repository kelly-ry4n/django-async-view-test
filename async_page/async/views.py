from django.shortcuts import render
from django.http import HttpResponse

import json


def home(request):

    return render(request,'home.html')

def get_data(request):

    return HttpResponse(json.dumps([1,2,3,4]))
