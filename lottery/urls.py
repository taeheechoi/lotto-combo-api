from django.urls import path
from .views import MegaMillionsList, PowerballList, WinningNumbersCombonationList
urlpatterns = [
    path('mega-millions/', MegaMillionsList.as_view()),
    path('powerball/', PowerballList.as_view()),
    path('winning-numbers-combinations/', WinningNumbersCombonationList.as_view()),

]
