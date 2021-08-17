import json
from itertools import combinations
import time
from datetime import datetime
from threading import Thread

import requests
from megamillions.models import MegaMillions, WinningNumbersCombination

url = 'https://data.ny.gov/api/views/5xaw-6ayf/rows.json?accessType=DOWNLOAD'


def delete_winning_numbers() -> None:
    MegaMillions.objects.all().delete()


def delete_winning_numbers_combinations() -> None:
    WinningNumbersCombination.objects.all().delete()


def winning_numbers_combinations_occurrences(win_nums_combos_list: list) -> dict:
    occurrences = {}
    for combo in win_nums_combos_list:
        try:
            occurrences[combo] += 1
        except:
            occurrences[combo] = 1
    return occurrences


def winning_numbers_combinations(win_nums_list: list) -> list:
    win_nums_combos_list = []

    for winning_numbers in win_nums_list:
        for i in range(1, len(winning_numbers)+1):
            for combo in combinations(winning_numbers, i):
                win_nums_combos_list.append(combo)

    return win_nums_combos_list


def load_winning_numbers(win_nums_data: list) -> None:
    # 2013-04-30T00:00:00
 
    load_data = [MegaMillions(draw_date=item[8], winning_numbers=item[9],
                              mega_ball=item[10], multiplier=item[11], number_of_draws=len(win_nums_data)) for item in win_nums_data]
    MegaMillions.objects.bulk_create(load_data)


def load_winning_numbers_combinations(win_nums_data: list) -> None:

    win_nums_list = [  # ('01', '09', '17', '27', '34', '*24') * mega number
        (*item[9].split(' '), f'*{item[10]}') for item in win_nums_data]

    win_nums_combos_list = winning_numbers_combinations(win_nums_list)

    win_nums_occurs = winning_numbers_combinations_occurrences(
        win_nums_combos_list)

    win_nums_occurs_data = [WinningNumbersCombination(winning_numbers_combination=', '.join(
        k), winning_numbers_combination_occurrence=v) for k, v in win_nums_occurs.items() if v >= 2]
    
    WinningNumbersCombination.objects.bulk_create(win_nums_occurs_data)


def get_winning_numbers(url: str) -> list:
    request = requests.get(url)
    data = json.loads(request.content.decode('utf-8'))["data"]
    return data


def run() -> None:
    Thread(delete_winning_numbers()).start()
    Thread(delete_winning_numbers_combinations()).start()

    # start = time.time()

    win_nums_data = get_winning_numbers(url)
    
    Thread(load_winning_numbers(win_nums_data)).start()
    Thread(load_winning_numbers_combinations(win_nums_data)).start()
    # print(time.time() - start)