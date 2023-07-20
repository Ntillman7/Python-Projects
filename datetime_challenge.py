from datetime import *
import pytz

format = "%H"

def PortlandTime():
    portland = datetime.now()
    portlandTimeZone = pytz.timezone('US/Pacific')
    portlandTime = portland.astimezone(portlandTimeZone)
    convert_portlandTime = (portlandTime.strftime(format))#converts to format with only hour
    int_portlandTime = int(convert_portlandTime)
    print(convert_portlandTime)


def NYCTime():
    nyc =datetime.now()
    nycTimeZone = pytz.timezone('US/Eastern')
    nycTime= nyc.astimezone(nycTimeZone)
    convert_nycTime =int(nycTime.strftime(format))
    print(convert_nycTime)


def LondonTime():
    london = datetime.now()
    londonTimeZone = pytz.timezone('GMT')
    londonTime = london.astimezone(londonTimeZone)
    convert_londonTime = int(londonTime.strftime(format))
    print(convert_londonTime)


PortlandTime()
NYCTime()
LondonTime()


def Open_Closed_Portland():
    if PortlandTime() < 9:
        print("Sorry, we are closed.")
    elif PortlandTime() > 17:
        print("Sorry, we are closed.")
    else:
        print('We are open!')

        
Open_or_Closed()
