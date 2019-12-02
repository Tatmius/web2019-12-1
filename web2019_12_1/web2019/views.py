from django.shortcuts import render
from django.http import HttpResponse
import web2019.models as models


# Create your views here.





def viewFunction(request):
  template_name = "index.html"
  context = {"text" : models.random_scrape()}
  return render(request,template_name,context)