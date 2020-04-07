#script to calculate the april's fool day
from datetime import date
from datetime import timedelta

def main():
    today = date.today()
    afd = date(year=today.year,month=4,day=1)

    if(afd<today):
        print("April fools day passed by %d days"%(today-afd).days)
        afd = afd.replace(year=today.year+1)

    print("April fools day in %d days"%(afd-today).days)


main()