from django.db import models

# Create your models here.
class MegaMillions(models.Model):
    draw_date = models.DateTimeField(null=False, blank=False)
    winning_numbers = models.CharField(max_length=20, null=False, blank=False)
    mega_ball = models.CharField(max_length=3, null=False, blank=False)
    multiplier = models.CharField(max_length=3, null=True, blank=True)
    number_of_draws = models.IntegerField(null=False, blank=False)

    # class Meta:
    #      ordering: ['-draw_date']

    def __str__(self):
        return f'draw_date:{self.draw_date} winning_numbers:{self.winning_numbers} mega_ball:{self.mega_ball} multiplier:{self.multiplier}'


class WinningNumbersCombination(models.Model):
    winning_numbers_combination = models.CharField(max_length=20, null=False, blank=False)
    winning_numbers_combination_occurrence = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'winning_numbers_combination:{self.winning_numbers_combination} winning_numbers_combination_occurrence:{self.winning_numbers_combination_occurrence}'
