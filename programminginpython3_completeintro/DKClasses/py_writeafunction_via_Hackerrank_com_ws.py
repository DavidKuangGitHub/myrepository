#py_writeafunction_via_Hackerrank_com_ws.py We add a Leap Day on February 29 alomost every four years...
#Example Input:
#1990
#Example Output:
#False
#Not leapyear : 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600, 
#Leap year: 1600, 2000, 2400  

def is_leap(year):
     return year % 4 == 0 and (year % 400 == 0 or year % 100 !=0 )

print("Enter the year you want to check: ")
myYear = int(input())
print("Results:")
print(is_leap(myYear))
