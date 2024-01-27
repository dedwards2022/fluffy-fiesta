# User inputted current hour, minute, seconds, and hours till alarm goes off
current_hour = int(input("Input current hour (0-23): "))
current_minute = int(input("Input current minutes (0-59): "))
current_second = int(input("Input current seconds (0-59):"))
alarm_set = int(input("Input hours until alarm goes off: "))

time = "{:02d}:{:02d}:{:02d}".format(current_hour, current_minute, current_second)
print("You inputed:", time)

future_hour = ((current_hour + alarm_set) % 24)

alarm_time = "{:02d}:{:02d}:{:02d}".format(future_hour, current_minute, current_second)
print("Alarm will go off: ", alarm_time)
