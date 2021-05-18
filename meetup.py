import datetime
import calendar


def meetup(year: int, month: int, week: str, day_of_week: str):
    """Return a date object that fits the date of the description."""
    date = datetime.date(year, month, 1)  # first day of the month
    # print(date) # 2013-04-01
    # print(calendar.day_name[date.weekday()])  # Name of first day of month
    # print(calendar.monthrange(date.year, date.month)[1]) # number of days in month

    # for num in range(1, calendar.monthrange(date.year, date.month)[1] + 1):
    #     print(num)

    date_to_return = datetime.date(year, month, 1)

    occurence = 0

    # go through all the days in the month
    for num in range(1, calendar.monthrange(date.year, date.month)[1] + 1):
        # new datetime object for each day in the month
        new_day = datetime.datetime(year, month, num)
        # print(num)
        new_day_of_week = calendar.day_name[new_day.weekday()]
        if day_of_week == new_day_of_week:
            occurence += 1

        # print(occurence)
        # print(new_day_of_week)
        # print(day_of_week == new_day_of_week)
        if day_of_week == new_day_of_week:
            if week == "1st" and occurence == 1:
                date_to_return = datetime.date(year, month, num)
                break
            elif week == "2nd" and occurence == 2:
                date_to_return = datetime.date(year, month, num)
                break
            elif week == "3rd" and occurence == 3:
                date_to_return = datetime.date(year, month, num)
                break
            elif week == "teenth" and str(new_day.day)[0] == "1" and occurence >= 2:
                date_to_return = datetime.date(year, month, num)
                break
            elif week == "4th" and occurence == 4:
                date_to_return = datetime.date(year, month, num)
                break
            elif week == "last" and occurence == 5:
                date_to_return = datetime.date(year, month, num)
                break

    return date_to_return


def MeetupDayException():
    return None


# meetup(2013, 4, "teenth", "Tuesday")  # date(2013, 4, 16)

# print(meetup(2013, 8, "1st", "Wednesday"))  # date(2013, 8, 7)
# print(meetup(2013, 6, "teenth", "Wednesday")) # date(2013, 6, 19))
print(meetup(2013, 2, "teenth", "Wednesday"))  # date(2013, 2, 13))
