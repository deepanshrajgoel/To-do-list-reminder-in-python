# -----------------------------------Modules you need------------------------------------ 
import pandas as pd
import datetime
from plyer import notification
import time

df = pd.read_excel("TO_DO_LIST") #Reading the xlsx file.

#-----------------------------------Creating Functions------------------------------------

def notify(name,description): #This Function will send you the desktop Notification.
    notification.notify(title = name,message=  description,app_icon="hel.ico",app_name="Reminder",timeout=15)
def main(): #The Main function for doing the stuff.
    Time_now=datetime.datetime.now().strftime("%H:%M:%S")
    for item in df.iterrows():  #The for loop will iterate the excel file.

        #------------------------Reading The File---------------------------------------

        Time_of_task= item['When you want to be reminded '].strftime("%H:%M:%S")
        Name_of_task = item['Name  of the task']
        Desc_of_task= item['Details']
        #Comparing the current time with the time of reminding
        if(Time_now==Time_of_task): 
            notify(Name_of_task,Desc_of_task)
            time.sleep(60)

if __name__ == "__main__":
    while(1): #infinitee loop
        main() 

#Made by ==> Deepansh Raj Goel
#For any queries join me on instagram ==> @deepanshrajgoel
#                Or mail me at        ==> deepanshrajgoel@hotmail.com
#Happy Coding ^___^