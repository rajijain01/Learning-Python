#in order to do a date/time calculation, the datetime module must first be imported.
# Then, todays date, as indicated by the built-in today() method, needs to be captured.
#short date formats use the lowercse letters for month, day and year.
#following is the example.

import datetime
currentDate = datetime.date.today()

strDueDate = input("Enter a due date in mm/dd/yy format")
dueDate = datetime.datetime.strptime(strDueDate,'%m/%d/%y').date()

daysLeft = dueDate - currentDate

print(f'You have {daysLeft} days left to finish')
