from base.base_function import function_base
import abc
import time

class function(function_base):
    
    def __init__(self):
        pass
    
    
    @abc.abstractmethod
    def func_run(self,params):
        try:
            ts = params[0]
            if ts == "now":
                ts = int(time.time())
            time_array = time.localtime(ts)
            date = time.strftime("%Y-%m-%d %H:%M:%S",time_array)
            print(date)
        except Exception as err:
            print(err)
            
            
        