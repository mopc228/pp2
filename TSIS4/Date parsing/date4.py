import datetime
current_date = datetime.datetime.now()
diff = int(input("Введите желаемую разницу дней: "))
other_date = current_date + datetime.timedelta(days = diff)
sec_diff = abs(current_date - other_date).total_seconds()
print(sec_diff)