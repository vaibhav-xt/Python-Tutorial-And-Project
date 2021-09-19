# Healthy programmer
""" Water - Water.mp3 (3.5 litre) - Drank - log
    Eyes - eyes.mp3 - every 30 min - EyDone - log
    Physical activity - physical.mp3 - 45 min - Exdone - log
"""
from datetime import datetime
from pygame import mixer
from plyer import notification
import time


def humanactivity(music):
    lst = ["Drank", "Eyedone", "Exerdone"]
    mixer.init()
    mixer.music.load(music)
    mixer.music.play(-1)
    input_to_stop = input()
    input_to_stop = input_to_stop.capitalize()
    if input_to_stop in lst:
        mixer.music.stop()
    else:
        print("Try Again!")
        humanactivity(music)

def write(message):
    with open("Routine.txt", "a") as f:
        f.write(f"{message} {datetime.now()}\n")
    f.close()

if __name__ == '__main__':
    water_to_drink = 3500
    water_drink = 0
    eye_exercise = 7
    eye_done = 1
    physical_activity = 7
    physical_done = 1
    round = 1
    day = 1
    while True:
        if water_drink != water_to_drink and eye_done != eye_exercise and physical_done != physical_activity:
            print(f"     Round {round}")
            if water_drink <= water_to_drink:
                time.sleep(10)
                notification.notify(
                    title="Drink water!",
                    message="Water is your body's principal chemical component and makes up about 50% to 70% of your body weight.",
                    app_icon="C:\\Users\\REX TERIA\\PycharmProjects\\py-1\\glass.ico",
                )
                print("Drinking Water. To Stop Music write 'Drank'!")
                humanactivity('drink water.mp3')
                write("Drank Water At: ")
                water_drink = water_drink + 500

            if eye_done <= eye_exercise:
                time.sleep(5)
                notification.notify(
                    title="Rest To You Eye!",
                    message="Eye is everything for us.",
                    app_icon="C:\\Users\\REX TERIA\\PycharmProjects\\py-1\\eye.ico",
                )
                print("Rest to your Eyes. To Stop Music write 'Eyedone'")
                humanactivity("Eye-Water.mp3")
                write("Rest To Your Eyes Done: ")
                eye_done = eye_done + 1

            if physical_done <= physical_activity:
                time.sleep(5)
                notification.notify(
                    title="Its Time To Do Exercise",
                    message="Keep Doing for you health as per notification.",
                    app_icon="C:\\Users\\REX TERIA\\PycharmProjects\\py-1\\meditation.ico",
                    )
                print("Do Exercise. To Stop Music write 'Exerdone'")
                humanactivity("Exercise Music.mp3")
                write("Exercise Done: ")
        else:
            write(f"Day {day} Task Completed. Well Done! \n\n")
            print(f"Day {day} Task Completed. Well Done! ")
            day = day + 1
            break
        round = round + 1
