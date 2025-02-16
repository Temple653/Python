from datetime import datetime 

od= datetime.today()
td=  od.year
md = od.month
odd= od.day

year = int(input("year "))
month = int(input("month "))
day = int(input("Day "))

nw = td- year

dm = 12 - month
#

nw = td- year
ndm= md + dm

if ndm > 11:

    ndm -=12
elif ndm >0:
    nw-=1




hmm= odd-day

print(f"you are {nw} years, {ndm} months and {hmm} days old")




    





