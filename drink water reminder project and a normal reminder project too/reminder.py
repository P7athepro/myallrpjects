import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
        title="Your device is saying you to stop coding",
        message="Hmm, I think so you have code enough you should go and study now",
        timeout=15,
            app_icon="D:\My_Data\Projects\drink water reminder project and a normal reminder project too\laptop.ico"
        )
        time.sleep(7200)