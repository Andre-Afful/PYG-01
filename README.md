# PYG-01
A Time Tracking Program

INTRODUCTION
Nana is a business man who has a consultancy firm. As a result, he charges a fixed rate per hour for every task that he carries out for his clients. Nana has realised that to make his work easier, he needs a Time Tracker program that will enable him to enter the time at which he started and ended a task, and with that information calculate the amount of money he earns within that period. A program was designed by the Azubi PYG-01 team that would enable Nana to achieve this.

PROGRAM IMPLEMENTATION
The Time Tracker is console based program  that has been designed to track the start time and end time entered by the user, this gives a result of the number of hours a task was carried out by the usser, and then calculates the amount of money made in tackling the task.

DESIGN PROCESS
1. The first step of the process was to define the problem. In this case, Nana who is a businessman, after meeting with clients would have to calculate by himself;
  a. The date and time which he started working to be able to calculate the number of hours he worked for a particular client
  b. With the number of hours he can calculate the amount the money he makes by multiplying the number of hours worked with his rate which is $5.
  c. For the purpose of simplyifing this task, accuracy and possibly integrity for audit purposes, Nana requires a program that can cary out this task correctly and efficiently.
2. The second step was to collect information. In this step, the PYG-01 team had to find out exactly what information was going to be input in the time tracking program, and the expected output. In this case the information that the program required was the date of the task, the time the task was initiated and closed, the number of hours, and finally the amount of money earned calculated from the number of hours worked. We decided to add another field for the different clients that the user deals with, that way the user can reference the logs to match a particular client to the respective data.

3. BRAINSTORMING
 The main aim of the PYG-01 team was to make sure the program was user-friendly and worked efficiently. As a result we had to think of various functions to write the program to enable it yield the desired result. The first program we wrote required the user to input both the date and time started, as well as the date and time the task ended. Upon further scrutiny, we managed to write a code for the program that would require the user to only enter the start time and end time in the 24hr format, i.e the hour and the minute(HH:MM). The program goes further to retrieve the system's date and time for the calculation of the number of hours worked and the money earned. Using the system's date and time ensured that there were no human error.  

DEVELOPING THE SOLUTION
The Time Tracker Program was written using python programming language. the steps below outline the though process in writing the program
steps:
1.  The libraries  required to incorporate the necessary functions were imported and they include CSV, DateTime, pandas and os
2.	A csv file was created to save our data
3.	The columns in the CSV files were converted to dataframe
4.	getDateTime was used to get the date and time in real time
5.	The date and time were then combined using combineDateTime
6.	The addToCSV function was used to add the data into the CSV file
7.	User input was created that tells your client "Enter the Client_ID: "
8.  The user will enter the client ID and he receives a prompt that reads “enter start time”
9.	The user will enter the start time and he receives a prompt that reads “enter stop time”
10.	After the user enters the stop time, At the backend, the program calculates the amount of time elapsed in hours by subtracting the end time from the start time
11.	It then multiply the amount of time elapsed by 5 to get the total amount spant in dollars 
12.	The following columns were added to the CSV: getDateTime()[0], Client_ID, time_started, time_ended, no_of_hours, money_earned)

PROGRAM DEPENDENCIES
1. The datetime library was used to provide a class for updating and dealing with dates and time
2. The os libary module provide functions which helped us in formatting and editing a directory. Some of these include, removing a folder's contents and also identifying a  current directory.
3. Again, we imported csv files to enable us sore large number of variables and data.
4.Some advantages of pandas include: it contains multiple methods for convenient data filtering. The major reason for our importation of pandas was because of its variety of utilities which can perform basic input and outout operations in a seamless manner.
5.Finally, Github served as a graphical interface for us to share our framework with others and also submit our assignment..


  







