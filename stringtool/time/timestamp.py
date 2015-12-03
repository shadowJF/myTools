import time

class timestamp:
    
    def __init__(self,var,type):
        if type == "timestamp":
            self.date = var
            self.ts = None
        elif type == "date":
            self.ts = int(var)
            self.date = None
            
    def get_timestamp(self):
        try:
            if not self.ts:
                if self.date == "now":
                    self.ts = int(time.time())
                else:
                    timeArray = time.strptime(self.date, "%Y%m%d%H%M%S")
                    self.ts = int(time.mktime(timeArray))
            print(self.ts)
        except Exception as err:
            print(err)
    
    def get_date(self):
        try:
            if not self.date:
                if self.ts == "now":
                    self.ts = int(time.time())
                timeArray = time.localtime(self.ts)
                self.date = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
            print(self.date)
        except Exception as err:
            print(err)
            