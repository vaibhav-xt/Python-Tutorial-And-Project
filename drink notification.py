# Drinking Water Notification
import time
from plyer import notification
i = 2
s = 0
while s < i:
    if __name__ == '__main__':
        notification.notify(
            title="Drink Water",
            message="Water is your body's principal chemical component and makes up about 50% to 70% of your body weight.",
            app_icon="C:\\Users\\REX TERIA\\PycharmProjects\\py-1\\glass.ico",
            timeout=5,
            ticker= 14
        )
        time.sleep(15)
    s = s + 1