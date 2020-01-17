"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# User input
args = sys.argv
# args
today = datetime.now()
month = today.month
year = today.year

cal = calendar.TextCalendar()

# if default cal if no input
if len(args) == 1:
    print("Here is the current calendar: ")
    cal.prmonth(year, month)
# elif 1 arg, assume month with current year
elif len(args) == 2:
    month = int(args[1])
    cal.prmonth(year, month)
    # elif 2 arg, assume month and year, return both
elif len(args) == 3:
    month = int(args[1])
    year = int(args[2])
    cal.prmonth(year, month)
# else print description for using program
else:
    print("Input should be: `py 14_cal.py month [year]`")
    # exit program
