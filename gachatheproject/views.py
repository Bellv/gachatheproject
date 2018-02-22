from django.shortcuts import render
from django.views.generic import TemplateView

import os
class IndexView(TemplateView):
    template = 'index.html'
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print (PROJECT_ROOT)
    print ('belly')
    def get(self, request):

        return render(
            request,
            self.template
        )
