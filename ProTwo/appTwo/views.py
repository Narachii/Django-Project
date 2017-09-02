from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(renduest):
	return HttpResponse("<em> My Second Project</em>")