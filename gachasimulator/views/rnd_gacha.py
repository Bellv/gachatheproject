from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Character


class GenerateGachaView(TemplateView):
    template = 'generate_gacha.html'

    def get(self, request):
        characters = Character.objects.all()

        return render(
            request,
            self.template,
            {
                'characters': characters
            }
        )

