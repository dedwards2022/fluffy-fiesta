# User inputted current hour, minute, seconds, and hours till alarm goes off
current_hour = int(input("Input current hour (0-23): "))
current_minute = int(input("Input current minutes (0-59): "))
current_second = int(input("Input current seconds (0-59):"))
alarm_set = int(input("Input hours until alarm goes off: "))

# Formats the user inputted hour, minute, second and outputs it to the screen
time = "{:02d}:{:02d}:{:02d}".format(current_hour, current_minute, current_second)
print("You inputed:", time)

# Calculates inputted hour to hours until alarm goes off with % 24 (24-hour)
future_hour = ((current_hour + alarm_set) % 24) 

# Formats outputted alarm clock  and prints it to the screen
alarm_time = "{:02d}:{:02d}:{:02d}".format(future_hour, current_minute, current_second)
print("Alarm will go off: ", alarm_time)
