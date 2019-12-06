from django.shortcuts import render
from django.http import HttpResponse
import web2019.models as models


# Create your views here.



def viewFunction(request):
  que=request.POST.get("pushed")
  template_name = "index.html"
  soup=models.random_scrape()
  mainText=models.getMainText(soup)
  title=models.getTitle(soup)
  context = {
    "title":title,
    "text" : mainText
  }
  return render(request,template_name,context)