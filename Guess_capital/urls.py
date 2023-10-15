from django.urls import path
from .views import GuessCapital

app_name = 'Guess_capital'


urlpatterns = [
    path('', GuessCapital.as_view(), name="guess_capital")
]
