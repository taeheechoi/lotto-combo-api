from megamillions.serializers import MegaMillionsSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import MegaMillionsSerializer, WinningNumbersCombinationSerializer
from .models import MegaMillions, WinningNumbersCombination

# Create your views here.


class MegaMillionsList(ListAPIView):
    queryset = MegaMillions.objects.all().order_by('-draw_date')
    serializer_class = MegaMillionsSerializer


class WinningNumbersCombonationList(ListAPIView):
    queryset = WinningNumbersCombination.objects.all().order_by(
        '-winning_numbers_combination_occurrence')
    serializer_class = WinningNumbersCombinationSerializer

    def get_queryset(self):
        queryset = WinningNumbersCombination.objects.all().order_by('-winning_numbers_combination_occurrence')
        numbers = self.request.query_params.get('numbers')
        quick_pick = self.request.query_params.get('quick-pick')
        if numbers is not None:
            queryset = queryset.filter(winning_numbers_combination__icontains=numbers).order_by('-winning_numbers_combination_occurrence')
        if quick_pick is not None:
            queryset = queryset.filter(quick_pick=quick_pick).order_by('-winning_numbers_combination_occurrence')
        return queryset
