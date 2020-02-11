#from datetime import date
from datetime import datetime
import sys
import time, logging



now = datetime.now()
print("Today's date and time = ", now)
#dateandtime_string = now.strftime("%d%m%Y %H:%M:%S")
dateandtime_string = now.strftime("%B %d, %Y %H:%M:%S")
print("Today's date and time in format is ", dateandtime_string)
#today = date.today()

#print("Today is date:", today)