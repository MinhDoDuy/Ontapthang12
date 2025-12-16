from datetime import datetime, timedelta

def today():
    return datetime.now().strftime("%d/%M/%y %H:%M:%S")

def add_days(day):
    return (datetime.now() + timedelta(days=day)).strftime("%d/%M/%y %H:%M:%S") #day là số ngày mình cộng thêm với ngày bây giờ