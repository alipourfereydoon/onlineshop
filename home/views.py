from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        self.request.session['my name']="amir"
        return context
    
    
    

    

  