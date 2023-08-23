from datetime import *
import pytz

format = "%H"#formats date to only show the hour, didnt use in this code just for reference

def PortlandTime():
    portland = datetime.now()#gets the time for right now
    portlandTimeZone = pytz.timezone('US/Pacific')#gets the timezone
    portlandTime = portland.astimezone(portlandTimeZone)#gets the time for the above chosen time zone
    return portlandTime.hour#must return hour to use in the if statment


def NYCTime():
    nyc =datetime.now()
    nycTimeZone = pytz.timezone('US/Eastern')
    nycTime= nyc.astimezone(nycTimeZone)
    return nycTime.hour

def LondonTime():
    london = datetime.now()
    londonTimeZone = pytz.timezone('GMT')
    londonTime = london.astimezone(londonTimeZone)
    return londonTime.hour


def Open_Closed():
    if PortlandTime() < 9:#opening time
        print("Portland branch is closed.")
    elif PortlandTime() > 17:#closing time
        print("Portland branch is closed.")
    else:
        print('Portland branch is open!')

    if LondonTime() < 9:
        print("London branch is closed.")
    elif LondonTime() > 17:
        print("London branch is closed.")
    else:
        print('London branch is open!')

    if NYCTime() < 9:
        print("New York City branch is closed.")
    elif NYCTime() > 17:
        print("New York City branchis closed.")
    else:
        print('New York City branch is open!')


if __name__ == "__main__":
    Open_Closed()
