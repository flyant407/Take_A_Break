# -*- coding: utf-8 -*-
import subprocess
import time
import easygui
import webbrowser

count = 1
#1 hour
work_time = (1*60*60)
#10 min
break_time = (10*60)

#get current time
now_time_hour = time.localtime(time.time()).tm_hour

#show the welcome message according to Real time
if((now_time_hour >= 6) and (now_time_hour < 11)):
    print("Good morning!!!!")
elif((now_time_hour >= 11) and (now_time_hour < 13)):
    print("Good noon!!!!")
elif((now_time_hour >= 13) and (now_time_hour < 18)):
    print("Good afternoon!!!!")
else:
    print("Good night!!!!")

#open the tasks which setted 
subprocess.Popen(r"D:\Downloads\sw\byhhbbs\byhh.exe")
time.sleep(5)
subprocess.Popen(r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")
time.sleep(5)
webbrowser.open("www.163.com")
time.sleep(5)

#This is pre-work time to read email, news and bbs...... 
while True:
    time.sleep(break_time)
    res = easygui.ynbox('Start to work?', 'Kinedly remind', ('Yes', 'No'))
    if(res == True):
        break

#From here main loop start    
print ("Start work from: " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
subprocess.Popen(r"D:\Program Files (x86)\SciTools\bin\pc-win32\understand.exe")
time.sleep(5)
while True:
    
    #work duration
    t = (work_time/count)
    time.sleep(t)
    res = easygui.ynbox('Take A Break?', 'Frome Break', ('Yes', 'No'))

    if (res == True):
        count = 1
        print ("     Break from: " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
        item = easygui.buttonbox("Choose a item", "ITEMS", ("music","website"))
        if (item == "music"):
            subprocess.Popen(r"D:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe")
        elif (item == "website"):
            webbrowser.open("www.baidu.com")

        #break duration
        time.sleep(break_time)
        res = easygui.ynbox('Start to work?', 'Frome Work', ('Yes', 'No'))
        if(res == False):
            time.sleep(break_time)
        print ("      Break end: " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
        print ("Start work from: " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

    else:
        easygui.msgbox("Workaholic!!!")
        count = count + 1


