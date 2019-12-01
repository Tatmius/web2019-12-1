from django.shortcuts import render
from django.views.generic import TemplateView
from manager.models import *
# Create your views here.
class UnknownWordView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = super(UnknownWordView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)