"""If you cross a 490meterlong street in 7 minutes, calculate your
speed in meters per second. Print the answer without any decimal
point in it. Hint: Speed = Distance / Time"""

distance = 490  
time_minutes = 7
time_seconds = time_minutes * 60  # Convert time from minutes to seconds
speed = distance / time_seconds  # Calculate the speed in meters per second
print(int(speed))
