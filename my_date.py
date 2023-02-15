#in order to do a date/time calculation, the datetime module must first be imported.
# Then, todays date, as indicated by the built-in today() method, needs to be captured.
#short date formats use the lowercse letters for month, day and year.
#following is the example.import datetime

# currentDate = datetime.date.today()

# strDueDate = input("Enter a due date in mm/dd/yy format")
# dueDate = datetime.datetime.strptime(strDueDate,'%m/%d/%y').date()

# daysLeft = dueDate - currentDate

# print(f'You have {daysLeft} days left to finish')


# todays date
import datetime
today =datetime.date.today()
new_year = datetime.date(2022,1,1)
print(today)
print(new_year)

# Time object
noon = datetime.time(12, 0, 0)
print(noon)

# now
now= datetime.datetime.now()
print(now)

# Print from a start date to some end date
# the size of each step in days
day_delta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date + 7*day_delta

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)
