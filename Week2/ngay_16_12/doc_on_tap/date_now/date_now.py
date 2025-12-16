from datetime import datetime

def current_date_vn():
    return datetime.now().strftime("%d/%m/%Y")

def current_time():
    return datetime.now().strftime("%H:%M:%S")