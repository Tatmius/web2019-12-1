from django.shortcuts import render
from django.http import HttpResponse
import web2019.models as models


# Create your views here.





def viewFunction(request):
  template_name = "index.html"
  text=models.random_scrape()
  context = {"text" : text}
  return render(request,template_name,context)