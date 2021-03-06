#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
from datetime import datetime
import os
import csv
import pandas as pd

# create file.csv
def createCSV():
    # check if Nana_Time_Tracker.csv exists already
    if os.path.exists('./Nana_Time_Tracker.csv'):
        return
    # creates Nana_Time_Tracker.csv with columns sonl
    else:
        columns = pd.DataFrame(columns=['Date', 'Client_ID' , 'Time_Started', 'Time_Ended', 
                              'No_of_Hours', 'Money_Earned'])
        # save file.csv
        columns.to_csv('./Nana_Time_Tracker.csv')
        return

# get the date and time from the system
def getDateTime():
        date_time = datetime.now()
        date = date_time.date()
        time = date_time.time()
        return date, time

# combine the date and time 
def combineDateTime(date, time):
    date_time = datetime.combine(date, time)
    return date_time


# add parameters to Nana_Time_Tracker.csv
def addToCSV(date, Client_ID, time_started, time_ended, no_of_hours, money_earned):
    my_csv_list = ['',date, Client_ID, time_started, time_ended, no_of_hours, money_earned]
    my_csv_file = open('./Nana_Time_Tracker.csv', 'a')
    writer = csv.writer(my_csv_file, delimiter=',')
    writer.writerow(my_csv_list)
    my_csv_file.flush()
    my_csv_file.close()
    return 1


# In[ ]:





# In[ ]:




