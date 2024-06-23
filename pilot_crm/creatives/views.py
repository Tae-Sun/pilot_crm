from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from pilot_crm.creatives.models import Creative


# Create your views here.


class CreativeListView(LoginRequiredMixin, ListView):
    model = Creative


creative_list_view = CreativeListView.as_view()
