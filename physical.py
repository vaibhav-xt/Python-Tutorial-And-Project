from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musicloop("ikson.wav", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 20

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musicloop('drink water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > watersecs:
            print("Eye Exercise time. Enter 'doneeyes' to stop the alarm.")
            musicloop('funny.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eye Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity time. Enter 'donephy' to stop the alarm.")
            musicloop('ncs.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity at ")