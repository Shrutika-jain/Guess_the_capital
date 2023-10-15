from django.shortcuts import render
from django.views.generic.base import View
import requests


# Create your views here.

# Render Guess Capital Template
class GuessCapital(View):
    def get(self, request):
        return render(request, 'GuessCapital.html')
