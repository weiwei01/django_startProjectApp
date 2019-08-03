from django.shortcuts import render
from django.http import HttpResponse
import csv


# Create your views here.
def account(request, name):
	#return HttpResponse("Hello, world. You're at the polls index.")
	return HttpResponse('hi!'+name)
