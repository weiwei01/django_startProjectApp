from django.shortcuts import render
from django.http import HttpResponse
import csv


# Create your views here.
def send(request):
	a = {}
	a['firstname'] = "J"
	a['lastname'] = "LK"
	a['email'] = "JLK@abc.com"
	b = {}
	b['firstname'] = "E"
	b['lastname'] = "MM"
	b['email'] = "EMM@abc.com"
	allstudents = []
	allstudents.append(a)
	allstudents.append(b)
	
	context = {
		'allstudents':allstudents
	}
	return render(request, 'page_senttotemplate.html', context)
