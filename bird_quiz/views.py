from django.shortcuts import render
from django.http import HttpResponse
from .models import Bird

def index(request):
    bird_list = Bird.objects.order_by('common_name')[:10]
    output = ', '.join([b.common_name for b in bird_list])
    return HttpResponse(output)

def question(request):
    return HttpResponse("You're looking at a question")


