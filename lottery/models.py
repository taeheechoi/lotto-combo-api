from django.db import models

# Create your models here.


class MegaMillions(models.Model):
    draw_date = models.DateTimeField(null=False, blank=False)
    winning_numbers = models.CharField(max_length=20, null=False, blank=False)
    ball = models.CharField(max_length=3, null=False, blank=False)
    multiplier = models.CharField(max_length=3, null=True, blank=True)
    number_of_draws = models.IntegerField(null=False, blank=False)

    class Meta:
        ordering: ['-draw_date']

    def __str__(self):
        return f'draw_date:{self.draw_date} winning_numbers:{self.winning_numbers} mega_ball:{self.mega_ball} multiplier:{self.multiplier}'


class Powerball(models.Model):
    draw_date = models.DateTimeField(null=False, blank=False)
    winning_numbers = models.CharField(max_length=20, null=False, blank=False)
    ball = models.CharField(max_length=3, null=False, blank=False)
    multiplier = models.CharField(max_length=3, null=True, blank=True)
    number_of_draws = models.IntegerField(null=False, blank=False)

    class Meta:
        ordering: ['-draw_date']

    def __str__(self):
        return f'draw_date:{self.draw_date} winning_numbers:{self.winning_numbers} mega_ball:{self.power_ball} multiplier:{self.multiplier}'


class WinningNumbersCombination(models.Model):

    GAME_OPTIONS = [('megamillions', 'megamillions'),
                    ('powerball', 'powerball')]

    game = models.CharField(choices=GAME_OPTIONS, max_length=50)
    winning_numbers_combination = models.CharField(
        max_length=50, null=False, blank=False)
    winning_numbers_combination_occurrence = models.IntegerField(
        null=False, blank=False)
    number_of_draws = models.IntegerField(null=False, blank=False)
    possibility = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True)
    # to include lotto numbers generator
    top_occurrence = models.BooleanField(default=False)

    def __str__(self):
        return f'winning_numbers_combination:{self.winning_numbers_combination} winning_numbers_combination_occurrence:{self.winning_numbers_combination_occurrence}'
