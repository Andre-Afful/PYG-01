# PYG-01
A Time Tracking Program

INTRODUCTION
Nana is a business man who has a consultancy firm. As a result, he charges a fixed rate per hour for every task that he carries out for his clients. Nana has realised that to make his work easier, he needs a Time Tracker program that will enable him to enter the time at which he started and ended a task, and with that information calculate the amount of money he earns within that period. A program was designed by the Azubi PYG-01 team that would enable Nana to achieve this.

PRGRAM IMPLEMENTATION
The Time Tracker is console based program  that has been designed to track the start time and end time entered by the user, this gives a result of the number of hours a task was carried out by the usser, and then calculates the amount of money made in tackling the task.

DESIGN PROCESS
1.The first step of the process was to define the problem. In this case, Nana who is a businessman, after meeting with clients would have to calculate by himself;
  a. The date and time which he started working to be able to calculate the number of hours he worked for a particular client
  b. With the number of hours he can calculate the amount the money he makes by multiplying the number of hours worked with his rate which is $5.
  c. For the purpose of simplyifing this task, accuracy and possibly integrity for audit purposes, Nana requires a program that can cary out this task correctly and efficiently.
  
2.The second step was to collect information. In this step, the PYG-01 team had to find out exactly what information was going to be input in the time tracking program, and the expected output. In this case the information that the program required was the date of the task, the time the task was initiated and closed, the number of hours, and finally the amount of money earned calculated from the number of hours worked. 

STEPS
1.	We imported some libraries which included CSV, DateTime, pandas and os
2.	We created a csv file to save our data
3.	We converted the columns in the CSV files to dataframe
4.	We used getDateTime to get the date and time in real time
5.	We combined the date and time using combineDateTime
6.	We used addToCSV to add the data into the CSV file
7.	We created an input that allowed our client to "Enter the Client_ID: "
8.	Nana would enter the client ID and he receives a prompt that reads “enter start time”
9.	Nana then enters the start time and receives a prompt that reads “enter stop time”
10.	After Nana enters the stop time, from the backend, we calculate the amount of time elapsed in hours by subtracting the end time from the start time
11.	We then multiply the amount of time elapsed by 5 to get the total amount spent in dollars 
12.	Lastly, we added the following column to the CSV getDateTime()[0], Client_ID, time_started, time_ended, no_of_hours, money_earned)

PROGRAM DEPENDENCIES
1. The datetime library was used to provide a class for updating and dealing with dates and time

2. We imported the os module to provide functions which helped us in formatting and editing a directory. Some of these include, removing a folder's contents and also identifying a current directory.

3. Again, we imported csv files to enable us store large number of variables and data.

4.Some advantages of pandas include, it containing multiple methods for convenient data filtering. The major reason for our importation of pandas was because of its variety of utilities which could perform basic input and output operations in a seamless manner.

5. Finally, Github served as a graphical interface for us to share our framework with others and also submit our assignment.




  







