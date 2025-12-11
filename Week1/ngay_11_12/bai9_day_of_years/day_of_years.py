class Solution:
    def dayOfYears(self, date):
        from datetime import datetime

        d = datetime.strptime(date, "%Y-%m-%d") #chuyển một chuỗi (string) dạng ngày giờ thành đối tượng datetime.
        return d.timetuple().tm_yday
