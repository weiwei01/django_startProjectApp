from django.shortcuts import render

# Create your views here.
def show_graph(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'page_chart.html')