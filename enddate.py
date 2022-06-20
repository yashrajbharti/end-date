
import fileinput
import sys
import datetime
from datetime import timedelta 

text = "</begin></TimeSpan>"   # if any line contains this text, I want to modify the whole line.

x = fileinput.input(files="/Users/yashraj/Desktop/python/Located_Events.txt", inplace=1)
for line in x:
    if text in line:
        str = [ t for t in line.split() if t.startswith('2021-') ][0]
        y = str.split('-')[0]
        m = str.split('-')[1]
        d = str.split('-')[2]
        gdate = datetime.datetime( int(y), int(m), int(d))
        next = gdate + timedelta(days = 1) 
        new_text = "<TimeSpan><end>" + next.strftime('%Y-%m-%d') + "</end></TimeSpan>"
        line += new_text
    sys.stdout.write(line)
x.close()