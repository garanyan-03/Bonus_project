import time

t = input("Insert time (h:m:s) ")


parts = t.split(":")
hours = int(parts[0])
minutes = int(parts[1])
seconds = int(parts[2])

# Convert to seconds
total_seconds = hours * 3600 + minutes * 60 + seconds


while total_seconds >= 0:
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    print(f"{h:02}:{m:02}:{s:02}")
    time.sleep(1)
    total_seconds -= 1
