from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
import datetime
import json
from web3 import Web3, HTTPProvider
import os
from django.conf import settings
from django.templatetags.static import static

# Create your views here.

class HomeView(View):
    success_url = reverse_lazy('portafolioVirtual:home')
    template_name = 'portafolioVirtual/home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == "POST":

            return render(request, self.template_name)