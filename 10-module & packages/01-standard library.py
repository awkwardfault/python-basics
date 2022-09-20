# we can import mny modules in python just by usinig 'import'
# like:
import webbrowser as wb
import webbrowser
import math

# or a date-time module
import datetime
today = datetime.date.today()
print(today)  # prints today's date
# or if we want to know the time too:
today1 = datetime.datetime.today()
print(today1)
# there can be more functions in a library; we have to look at the documentations to find out more
#  we simply can not remember everything

# there's also a web-browser module in python
url = 'https://docs.python.org/3/'
webbrowser.open(url)

# alising: usin the word webbrowser to call a function everytime is a hassle so we can aliasing
url2 = 'https://www.w3schools.com/python/'
wb.open(url2)
