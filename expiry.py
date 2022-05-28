from datetime import date
today=date.today()

current_year=today.year
current_month=today.month
day=today.day


example_date="28/05/2022"
example_date_compare=example_date.split("/")



if current_year==int(example_date_compare[-1]) and current_month==int(example_date_compare[-2]) and day==int(example_date_compare[-3]):
    print("notification")
else:
    print("no product expired")
