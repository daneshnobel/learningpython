##formatting 

from datetime import datetime
from datetime import date
from datetime import timedelta
def main():
    # now = datetime.now()
    # print(now.strftime("%a"))
    # print(now.strftime("%A"))
    # print(now.strftime("%b"))
    # print(now.strftime("%B"))
    # print(now.strftime("%d"))
    today = date.today()
    # tomorrow = today+timedelta(days=1)
    tomorrow = date(year=today.year,month=today.month,day=today.day+1)
    print(tomorrow)
main()