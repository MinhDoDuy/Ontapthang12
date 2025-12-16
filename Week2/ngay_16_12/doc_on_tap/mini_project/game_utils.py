import random
from datetime import datetime

def start_game():
    number = random.randint(1, 100)
    start_time = datetime.now()
    return number, start_time

def end_game(start_time):
    end_time = datetime.now()
    play_time = end_time - start_time
    return end_time, play_time