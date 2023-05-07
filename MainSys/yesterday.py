from datetime import datetime
from datetime import date
from datetime import timedelta
 
 
today = date.today()
print("Today is: ", today)
 
# Get 2 days earlier
yesterday = today - timedelta(days = 2)
print("Day before yesterday was: ", yesterday)