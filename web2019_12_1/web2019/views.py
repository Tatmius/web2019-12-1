from django.shortcuts import render
from django.http import HttpResponse
import web2019.models as models


# Create your views here.

def hello_template(request):
    return render(request, 'index.html')

text=models.soup
def viewFunction(request):
  template_name = "index.html"
  context = {"text" : text} # <- "text"がテンプレート内での変数名
  return render(request,template_name,context)