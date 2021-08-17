from django.urls import path
from .views import MegaMillionsList, WinningNumbersCombonationList
urlpatterns = [
    path('', MegaMillionsList.as_view()),
    path('winning-numbers-combinations/', WinningNumbersCombonationList.as_view()),

]
