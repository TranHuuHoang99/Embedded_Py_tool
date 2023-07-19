import sys
import getopt

class Command(enumerate):
    year = ['-y', '--year']
    month = ['-mh', '--month']
    day = ['-d', '--day']
    hour = ['-h', '--hour']
    minute = ['-mt', '--minute']
    second = ['-s', '--second']

argv = sys.argv[1:]
otps, argvs = getopt.getopt(argv, "y:mh:d:h:mt:s:", ["year=", "month=", "day=", "hour=", "minute=", "second="])

year = 0
month = 0
day = 0 
hour = 0
minute = 0
second = 0

for otp, arg in otps:
    if otp in Command.year:
        year = arg
    elif otp in Command.month:
        month = arg
    elif otp in Command.day:
        day = arg
    elif otp in Command.hour:
        hour = arg
    elif otp in Command.minute:
        minute = arg
    elif otp in Command.second:
        second = arg
    else:
        print("Command error !!!")

print(year)
print(month)
print(day)
print(second)
 
    

