# Generated by Django 3.2.6 on 2021-08-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megamillions', '0009_remove_winningnumberscombination_number_of_draws'),
    ]

    operations = [
        migrations.AddField(
            model_name='winningnumberscombination',
            name='number_of_draws',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='winningnumberscombination',
            name='possibility',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
