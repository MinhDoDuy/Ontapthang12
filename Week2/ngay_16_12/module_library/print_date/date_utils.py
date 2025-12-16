from datetime import datetime, timedelta

def today():
    return datetime.now().strftime("%d/%m/%y - %H:%M:%S")

def add_days(day):
    return (datetime.now() + timedelta(days=day)).strftime("%d/%m/%y - %H:%M:%S")
    #day là số ngày mình cộng thêm với ngày bây giờ
    #Vì Python KHÔNG cho cộng trừ ngày giờ bằng số thường.
    #datetime là mốc thời gian, timedelta là khoảng cách giữa các mốc đó.