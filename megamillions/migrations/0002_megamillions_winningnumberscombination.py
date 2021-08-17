# Generated by Django 3.2.6 on 2021-08-17 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('megamillions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MegaMillions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.DateTimeField(db_index=True)),
                ('winning_numbers', models.CharField(max_length=20)),
                ('mega_ball', models.CharField(max_length=3)),
                ('multiplier', models.CharField(blank=True, max_length=3, null=True)),
                ('number_of_draws', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WinningNumbersCombination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winning_numbers_combination', models.CharField(max_length=20)),
                ('winning_numbers_combination_occurrence', models.IntegerField()),
            ],
        ),
    ]
