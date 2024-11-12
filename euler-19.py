
days = [
    'Sunday', 
    'Monday', 
    'Tuesday', 
    'Wendesday', 
    'Thursday',
    'Friday',
    'Saturday'
]

month_days = {
    1: 31,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

class Date:
    def __init__(self, month, day, year, weekday):
        self.month = month
        self.day = day
        self.year = year
        self.weekday = weekday

    def is_leap_year(self):
        year = self.year
        if year % 400 == 0: return True
        if year % 100 == 0: return False
        if year % 4 == 0: return True
        return False

    def get_next_month(self):
        return 1 if self.month == 12 else self.month + 1
    
    def get_next_day(self):
        if self.month != 2:
            return 1 if self.day >= month_days[self.month] else self.day + 1
        feb_days = 29 if self.is_leap_year() else 28
        return 1 if self.day >= feb_days else self.day + 1
    
    def get_next_year(self):
        return self.year + 1
    
    def get_next_weekday(self):
        next_index = days.index(self.weekday) + 1
        return days[next_index if next_index < len(days) else 0]
    
    def next_date(self):
        self.day = self.get_next_day()
        self.weekday = self.get_next_weekday()
        if self.day == 1:
            self.month = self.get_next_month()
            if self.month == 1:
                self.year = self.get_next_year()

    def __str__(self):
        month = f'0{self.month}' if self.month <= 10 else self.month
        day = f'0{self.day}' if self.day <= 10 else self.day
        return f'{self.month}-{self.day}-{self.year}'

def main():
    date = Date(month=1, day=1, year=1900, weekday='Monday')
    while date.year == 1900:
        date.next_date()
    count = 0
    while date.year <= 2000:
        print(f'{date} {date.weekday}')
        if date.day == 1 and date.weekday == 'Sunday':
            count += 1
        date.next_date()

    return count