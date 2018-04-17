from django.shortcuts import render
from django.views.generic import TemplateView

import os
class IndexView(TemplateView):
    template = 'index.html'

    def get(self, request):

        return render(
            request,
            self.template
        )
