from django.conf.urls import url

from . import views
from .views.fatego import GenerateGachaFGOView

urlpatterns = [
    url(r'^fatego$',
        GenerateGachaFGOView.as_view(),
        name='fgo_gacha'
    )
]
