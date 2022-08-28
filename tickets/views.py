
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import *
# Create your views here.

#1 without REST and no model query FBV
def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            "Name": "Omar",
            "mobile": 789456,
        },
        {
            'id': 2,
            'name': "yassin",
            'mobile': 74123,
        }
    ]
    return JsonResponse (guests, safe=False)


#2 no rest from model
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values()),
    }
    return JsonResponse(response)