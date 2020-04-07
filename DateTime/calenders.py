import calendar

def main():
    myCal = calendar.TextCalendar(calendar.MONDAY)
    calText = myCal.formatmonth(2020,1,0,0)
    print(calText)

main()

