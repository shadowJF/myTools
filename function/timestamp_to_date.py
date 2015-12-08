from base.base_function import function_base
import abc
import time

class function(function_base):
    
    def __init__(self):
        pass
    
    def check_params(self,params):
        if len(params) == 0:
            raise ValueError("Arguments error, no arguments added after function.")
        if params[0] != "now":
            if len(params[0]) != 10 and len(params[0]) !=13 :
                raise ValueError("timestamp format error, its length should be 10 or 13. length: " + str(len(params[0])))
                
        
    @abc.abstractmethod
    def func_run(self,params):
        try:
            ts = params[0]
            if ts == "now":
                ts = int(time.time())
            elif len(ts) == 13:
                ts = ts[0:10]
            time_array = time.localtime(int(ts))
            date = time.strftime("%Y-%m-%d %H:%M:%S",time_array)
            print(date)
        except Exception as err:
            print(err)
            
            
        