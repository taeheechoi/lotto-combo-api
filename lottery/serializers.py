from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import MegaMillions, Powerball, WinningNumbersCombination


class MegaMillionsSerializer(ModelSerializer):
    class Meta:
        model = MegaMillions
        # fields = '__all__'
        exclude = ('id',)

class PowerballSerializer(ModelSerializer):
    class Meta:
        model = Powerball
        # fields = '__all__'
        exclude = ('id',)

class WinningNumbersCombinationSerializer(ModelSerializer):
    class Meta:
        model = WinningNumbersCombination
        # fields = '__all__'
        exclude = ('id',)
