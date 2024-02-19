import datetime
current_time = datetime.datetime.now()
current_date = current_time.date()
yesterday = current_date - datetime.timedelta(days=1)
today = current_date
tomorrow = current_date + datetime.timedelta(days=1)
print("Yesterday was " + str(yesterday) + ".\n" + "Today is " + str(today) + ".\n" + "Tomorrow will be " + str(tomorrow) + ".")