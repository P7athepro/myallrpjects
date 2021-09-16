import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
        title ="Drink Water",
        message ="It is very important to drink water cause dehydration = laziness so drink a lot",
        timeout =10,
            app_icon ="D:\My_Data\Projects\drink water reminder project and a normal reminder project too\icon.ico",
        )
        time.sleep(60*60)