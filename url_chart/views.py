from django.shortcuts import render
from django.http import HttpResponse
import csv


# Create your views here.
def show_graph(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'page_url_chart.html')
def graph_data(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
	writer = csv.writer(response)
	writer.writerow(['salesperson','sales'])
	#tempList = []

	#tempList.append(output['name'])
	#tempList.append(output['negative'])
	#tempList.append(output['neutral'])
	#tempList.append(output['positive'])
	#writer.writerow(tempList)

	writer.writerow(['Bob','60'])
	return response