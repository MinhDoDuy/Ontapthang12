class Solution:
    def day_of_theweek(self, day, month, year):
        from datetime import datetime
        wd = datetime(year, month, day).weekday()
        names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Sunday', 'Saturday', 'Sunday']
        return names[wd]