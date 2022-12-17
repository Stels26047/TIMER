import time

sec = 1
minute = 1
h = 1

# Seconds
while True:
 if sec < 60: 
    time.sleep(1)
    print(f'{sec} sec')
    sec += 1
    if sec == 60:
        sec = 0
        break

# Minutes
while True:
    time.sleep(1)
    print(f'{minute} min {sec} sec')
    if sec == 59:
        minute += 1
        sec = sec - 60
    sec += 1
    if minute == 60:
        minute = 0
        sec = 0
        break

# Hours
while True:
    time.sleep(1)
    print(f'{h} h  {minute} min {sec} sec')
    if sec == 59:
        minute += 1
        sec = sec - 59
    sec += 1
    if minute == 60:
        minute = minute - 60
        h += 1
    if h == 24:
        break
