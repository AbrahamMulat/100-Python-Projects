# --- coding: utf-8 ---
# @FileName  :pomodoro.py
# @Time      :11/25/2022 7:04 PM
# @Author    :Abraham
# @Software  :PyCharm

import time


def count_down(time_in_second):
    while time_in_second:
        mins, secs = divmod(time_in_second, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # print(timer, end="\r")  # overwrite previous line, not working in python
        print(timer)
        time.sleep(1)
        time_in_second -= 1
    print("Time is up!!!")


t_in_sec = int(input("Enter the time in seconds: "))
count_down(t_in_sec)


def break_time():
    t = 5
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # print(timer, end="\r")
        print(timer)
        time.sleep(1)
        t -= 1


# pomodoro timer
def pomodoro():
    work_time = 10  # 25 minute for work
    break_t = 5  # 5 minutes for break
    print("Pomodoro started, start Working now!!")
    for i in range(2):  # four intervals of 25 minute work time followed by 5 minute break
        while work_time:
            mins, secs = divmod(work_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # print(timer, end="\r") # overwrite previous line, not working in pycharm
            print(timer)
            time.sleep(1)
            work_time -= 1
        print("Break Time!!")
        break_time()
        print("Work time!!")


# pomodoro()

