from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from first_app.models import Topic,Webpage, AccessRecord

def index(request):
	webpage_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records' : webpage_list}
	return render(request, 'first_app/index.html', context=date_dict)

