"""relatorio URL Configuration"""
from django.urls import path

from core.views import IndexView, IndexWeasyView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('relatorio/', IndexWeasyView.as_view(), name='index_weasy'),
]
