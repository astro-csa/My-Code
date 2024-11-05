def add_time(start, duration, day = False):
    # Separating the hours, the minutes and the time of the day for start
    start_hours = ''
    start_minutes = ''
    period = ''
    switch = True
    for digit in start:
        if switch:
            if digit == ':':
                switch = False
                continue
            start_hours += digit
        else:
            if digit.isdigit():
                start_minutes += digit
            if digit.isalpha() and digit != ' ':
                period += digit               
    # Separating the hours and the minutes for duration
    duration_hours = ''
    duration_minutes = ''
    switch = True
    for digit in duration:
        if switch:
            if digit == ':':
                switch = False
                continue
            duration_hours += digit
        else:
            duration_minutes += digit
    # Converting and adding the times
    new_minutes = int(start_minutes) + int(duration_minutes)
    new_hours = int(start_hours) + int(duration_hours) + new_minutes // 60
    new_minutes %= 60
    # Keep the two-digits format for minutes
    if new_minutes < 10:
        new_minutes = '0' + str(new_minutes)
    # Formating the period
    match period:
        case 'AM':
            period = 0
        case 'PM':
            period = 1
    # Adding the period changes
    period += new_hours // 12
    if new_hours > 12:
        # Properly formting 00:00 as 12:00
        if new_hours % 12 == 0:
            new_hours ='12'
        else:
            new_hours %= 12
    # If day is given
    if day:
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        # I could use the method .capitalize() too
        days_lower = [d.lower() for d in days]
        new_day = days[(days_lower.index(day.lower()) + period // 2) % 7]
    # Checking how many days in the future the date is
    if period // 2 == 0:
        next_day = ''
    if period // 2 == 1:
        next_day = '(next day)'
    if period // 2 > 1:
        next_day = f'({period // 2} days later)'
    # Returning to the correct period format
    period %= 2
    match period:
        case 0:
            period = 'AM'
        case 1: 
            period = 'PM'
    if day:
        new_time = (str(new_hours) + ':' + str(new_minutes) + ' ' + period  + ", " + new_day + ' ' + next_day).strip()
    else:
        new_time = (str(new_hours) + ':' + str(new_minutes) + ' ' + period + ' ' + next_day).strip()
    return new_time


add_time('3:30 PM', '2:12', 'Monday')