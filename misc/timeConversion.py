# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Input: a time string in hh:mm:ssAM/hh:mm:ssPM format
# Output: a time string in 24hr format

def timeConversion(s):
    period = s[-2:]
    time = s[0: len(s) - 2].split(':')
    
    if int(time[0]) == 12 and period == 'AM':
        time[0] = '00'
    elif int(time[0]) <= 11 and period == 'PM':
        time[0] = str(int(time[0]) + 12)
    
    return ':'.join(time)