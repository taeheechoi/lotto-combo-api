# Generated by Django 3.2.6 on 2021-08-17 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('megamillions', '0004_alter_winningnumberscombination_possibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winningnumberscombination',
            name='possibility',
        ),
    ]
