import datetime
current_time = datetime.datetime.now()
time_without_ms = current_time.replace(microsecond=0)
print(time_without_ms)
