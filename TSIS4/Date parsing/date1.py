import datetime
current_time = datetime.datetime.now()
current_date = current_time.date()
fivedaysago = current_date - datetime.timedelta(days=5)
print(fivedaysago)