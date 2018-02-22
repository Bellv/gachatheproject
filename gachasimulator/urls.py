from django.conf.urls import url

from . import views
from .views.rnd_gacha import GenerateGachaView

urlpatterns = [
    url(r'^$',
        GenerateGachaView.as_view(),
        name='generate_gacha'
    )
]
